#1_시퀀스투시퀀스

import pandas as pd
from fontTools.misc.cython import returns
from joblib.numpy_pickle_utils import BUFFER_SIZE
from keras.integration_test.preprocessing_test_utils import VOCAB_SIZE, BATCH_SIZE
from numpy.ma.core import count
from promise.promise import MAX_LENGTH
from tensorflow.python.keras.utils.version_utils import training

#1. 데이터수집
# 질문과 답변이 잇는 말뭉치를 가져오기
# Q질문 A답변 label(0일상다반사,1부정,2긍정)
corpus = pd.read_csv('https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv')
#확인
print(corpus['Q'].head()) #질문 열 의 상단 5개
print(corpus['A'].head()) #답변 열 의 상단 5개
#확인
print(f"Q : {corpus['Q'][0]}")
print(f"A : {corpus['A'][0]}")
#확인
print(corpus.shape) #차원확인
#샘플링(1000개사용)
texts = []
pairs = []

print(zip(corpus['Q'],corpus['A']))

for i , (text, pair) in enumerate(zip(corpus['Q'],corpus['A'])) :
    texts.append(text)
    pairs.append(pair)
    if i >= 1000 : #RAM문제로 1000개만
        break

# print(list(zip(texts,pairs))[1995:2000])

import re
def clean_sentence(sentence):
    sentence = re.sub(r'[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\t]'," ",sentence)
    return sentence

print(clean_sentence("안녕하세요~:)"))
print(clean_sentence("텐서플로!@#!$@!$"))

from konlpy.tag import Okt
okt = Okt()
def process_morph(sentence):
    return ' '.join(okt.morphs(sentence))

#한글 문장 전처리
def clean_and_morph(sentence, is_question=True):
    #한글 문장 전처리
    sentence = clean_sentence(sentence)
    #형태소 변환
    sentence = process_morph(sentence)
    # 질문인 경우, 답인 경우를 분기하여 처리
    if is_question :
        return sentence
    else :
        return (f'<START>  {sentence}', f'{sentence}  <END>')

def preprocess(texts,pairs):
    questions = []
    answer_in = []
    answer_out = []

    #질의에 대한 전처리
    for text in texts :
        question = clean_and_morph(text,is_question=True)
        questions.append(question)

    #답변에 대한 처리
    for pair in pairs :
    #전처리와 morph 수행
        in_,out_ = clean_and_morph(pair,is_question=False)
        answer_in.append(in_)
        answer_out.append(out_)
    return questions, answer_in, answer_out

questions,answer_in,answer_out = preprocess(texts,pairs)
print(questions[:2])
print(answer_in[:2])
print(answer_out[:2])

#전체 문장을 하나의 리스트로 만드릭
all_sentences = questions + answer_in + answer_out

#라이브러리 불러오기
import numpy as np
import warnings
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#WARNING 무시
warnings.filterwarnings('ignore')

tokenizer = Tokenizer(filters="",lower=False,oov_token='<OOV>')
tokenizer.fit_on_texts(all_sentences)

#단어 사전 확인
for word, idx in tokenizer.word_index.items():
    print(f'{word}\t -> \t{idx}')
    if idx > 10:
        break

#토큰 개수 확인
print(len(tokenizer.word_index))

#치환 : 텍스트를 시퀀스로 인코딩(texts_TO_sequences)
question_sequence = tokenizer.texts_to_sequences(questions)
answer_in_sequence = tokenizer.texts_to_sequences(answer_in)
answer_out_sequence = tokenizer.texts_to_sequences(answer_out)

#문장의 길이 맞추기(pad_sequences)
MAX_LENGTH = 30
question_padded = pad_sequences(question_sequence,maxlen=MAX_LENGTH,truncating='post',padding='post')
answer_in_padded = pad_sequences(answer_in_sequence,maxlen=MAX_LENGTH,truncating='post',padding='post')
answer_out_padded = pad_sequences(answer_out_sequence,maxlen=MAX_LENGTH,truncating='post',padding='post')

print(question_padded.shape)
print(answer_in_padded.shape)
print(answer_out_padded.shape)

from tensorflow.keras.layers import Embedding,LSTM,Dense,Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint

#인코더
class Encoder(tf.keras.Model) :
    def __init__(self,units,vocab_size,embedding_dim,time_steps):
        super(Encoder,self).__init__()
        self.embedding = Embedding(vocab_size,embedding_dim,input_length=time_steps)
        self.dropout = Dropout(0.2)
        self.lstm = LSTM(units,return_state = True)

    def call(self,inputs):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x,hidden_sate,cell_sate = self.lstm(x)
        return [hidden_sate,cell_sate]

# 디코더
class Decoder(tf.keras.Model) :
    def __init__(self,units,vocab_size,embedding_dim,time_steps):
        super(Decoder,self).__init__()
        self.embedding = Embedding(vocab_size,embedding_dim,input_length=time_steps)
        self.dropout = Dropout(0.2)
        self.lstm = LSTM(units,return_state = True, return_sequences=True)
        self.dense = Dense(vocab_size,activation='softmax')

    def call(self,inputs,initial_state):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x, hidden_sate, cell_state = self.lstm(x, initial_state=initial_state)
        x = self.dense(x)
        return x, hidden_sate,cell_state

# 모델 결합
class Seq2Seq(tf.keras.Model) :
    def __init__(self,units,vocab_size,embedding_dim,time_steps,start_token,end_token):
        super(Seq2Seq,self).__init__()
        self.start_token = start_token
        self.end_token = end_token
        self.time_steps = time_steps

        self.encoder = Encoder(units,vocab_size,embedding_dim,time_steps)
        self.decoder = Decoder(units,vocab_size,embedding_dim,time_steps)

    def call(self,inputs,training=True):
        if training :
            encoder_inputs, decoder_inputs = inputs
            context_vector = self.encoder(encoder_inputs)
            decoder_outputs,_,_ = self.decoder(inputs=decoder_inputs,initial_state = context_vector)
            return decoder_outputs

        else:
            context_vector = self.encoder(inputs)
            target_seq = tf.constant([[self.start_token]], dtype=tf.float32)
            results = tf.TensorArray(tf.int32, self.time_steps)

            for i in tf.range(self.time_steps) :
                decoder_output, decoder_hidden, decoder_cell = self.decoder(target_seq,initial_state=context_vector)
                decoder_output = tf.cast(tf.argmax(decoder_output, axis=-1),dtype=tf.int32)
                decoder_output = tf.reshape(decoder_output, shape=(1,1))
                results = results.write(i,decoder_output)

                if decoder_output == self.end_token :
                    break

                target_seq = decoder_output
                context_vector = [decoder_hidden,decoder_cell]

            return tf.reshape(results.stack(), shape=(1,self.time_steps))

VOCAB_SIZE = len(tokenizer.word_index)+1
def convert_to_one_hot(padded) :
    one_hot_vector = np.zeros((len(answer_out_padded),MAX_LENGTH,VOCAB_SIZE))

    for i, sequence in enumerate(answer_out_padded):
        for j, index in enumerate(sequence):
            one_hot_vector[i,j,index] = 1

    return one_hot_vector
answer_in_one_hot = convert_to_one_hot(answer_in_padded)
answer_out_one_hot = convert_to_one_hot(answer_out_padded)
print(answer_in_one_hot[0].shape)
print(answer_out_one_hot[0].shape)

def convert_index_to_text(indexs,end_token):
    sentence = " "

    for index in indexs:
        if index == end_token :
            break;
        if index > 0 and tokenizer.index_word[index] is not None:
            sentence += tokenizer.index_word[index]
        else :
            sentence += ""
        sentence += ""
    return  sentence


BUFFER_SIZE = 1000
BATCH_SIZE = 16
EMBEDDING_DIM = 100
TIME_STEPS = MAX_LENGTH
START_TOKEN = tokenizer.word_index['<START>']
END_TOKEN = tokenizer.word_index['<END>']

UNITS = 128

VOCAB_SIZE = len(tokenizer.word_index) +1
DATA_LENGTH = len(questions)
SAMPLE_SIZE = 3
NUM_EPOCHS = 20

checkpoint_path = 'model/seq2seq-chatbot-checkpoint.ckpt'
checkpoint = ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,monitor='loss',verbose=1)

#seq2seq
seq2seq = Seq2Seq(UNITS,VOCAB_SIZE,EMBEDDING_DIM,TIME_STEPS,START_TOKEN,END_TOKEN)
seq2seq.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])

def make_prediction(model,question_inputs):
    results = model(inputs=question_inputs, training=False)
    results = np.asarray(results).reshape(-1)
    return results

for epoch in range(NUM_EPOCHS) :
    print(f'processing epoch : {epoch * 10 + 1}...')
    seq2seq.fit([question_padded,answer_in_padded],
                    answer_out_one_hot,
                    epochs= 10,
                    batch_size=BATCH_SIZE,
                    callbacks=[checkpoint]
                )
    samples = np.random.randint(DATA_LENGTH,size=SAMPLE_SIZE)

    for idx in samples:
        question_inputs = question_padded[idx]
        results = make_prediction(seq2seq, np.expand_dims(question_inputs,0))
        results = convert_index_to_text(results,END_TOKEN)

        print(f'Q : {questions[idx]}')
        print(f'A : {results}\n')
        print()

def make_question(sentence) :
    sentence = clean_and_morph(sentence)
    question_sequence = tokenizer.texts_to_sequences([sentence])
    question_padded = pad_sequences(question_sequence,maxlen=MAX_LENGTH,truncating='post',padding='post')
    return question_padded
make_question("오늘 날씨 어때?")

#챗봇 함수
def run_chatbot(question):
    question_inputs = make_question(question)
    results = make_prediction(seq2seq,question_inputs)
    results = convert_index_to_text(results,END_TOKEN)
    return results

#챗봇실행
while True:
    user_input = input("<<말을 걸어 보세요! \n")
    if user_input == 'q':
        break
    print(">> 챗봇 응답 : {}".format(run_chatbot(user_input)))