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
texts = [] # 질문 리스트
pairs = [] # 답변 리스트

# for index , value in enumerate( 리스트/튜플 ) :
# for value in 리스트/튜플 :
print(zip(corpus['Q'],corpus['A']))

for i , (text, pair) in enumerate(zip(corpus['Q'],corpus['A'])) : #enumerate : 내장함수 #인덱스와 값을 동시에 접근하면서 반복문을 실행하려고할 때
    texts.append(text)
    pairs.append(pair)
    if i >= 1000 : #RAM문제로 1000개만
        break

# print(list(zip(texts,pairs))[1995:2000])

import re
def clean_sentence(sentence): #한글 , 숫자를 제외한 문자는 제거
    # 한글 , 숫자를 제외한 모든 문자는 제거
    # 1. re.sub(r'정규표현식', r'대체할문자' , 문자열 ) : 파이썬 내장용 문자열 정규표현식 함수
    # 2. pd['열이름'].str.replace("정규표현식","" , regex=True ) : 데이터프레임내 정규표현식 방법
    sentence = re.sub(r'[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\t]'," ",sentence)
    return sentence

print(clean_sentence("안녕하세요~:)")) #안녕하세요
print(clean_sentence("텐서플로!@#!$@!$")) #텐서플로

#한글 형태소 분석
from konlpy.tag import Okt
okt = Okt() # 형태소 분석 객체 생성

def process_morph(sentence):
    return ' '.join(okt.morphs(sentence)) # 형태소 분석 결과 목록 을 하나의 문자열 합치기
    # 형태소들 사이에 공백' ' 으로 구성한 문자열
print( '안녕하세요'.join(['유재석' , '강호동'] ) ) # '유재석안녕하세요강호동'

#한글 문장 전처리
# - 전처리 실행후 질문전체 , 답변시작 , 답변끝 구분
def clean_and_morph(sentence, is_question=True): # 매개변수명=초기값 : 매개변수에 초기값 넣기
    #한글 문장 전처리
    sentence = clean_sentence(sentence)
    #형태소 변환
    sentence = process_morph(sentence)
    # 질문인 경우, 답인 경우를 분기하여 처리
    # 질문(Question) 인 경우 , Answer(답변) 인 경우를 구분하여 처리
    if is_question :
        return sentence
    else : # 프로그래밍 언어에서 함수는 무조건 리턴(결과) 1개 이다.
        return (f'<START>  {sentence}', f'{sentence}  <END>')  # ( 값1 , 값2 ) : 튜플 형식 # ( )생략 가능

# - 질문전체 , 답변시작 , 답변끝 리스트 만들기
def preprocess(texts,pairs):
    questions = [] # 인코더에 입력할 질문 전체 리스트
    answer_in = [] # 디코더에 입력할 답변의 시작 , <START> 토큰을 문장 처음에 추가 , # 데이터들을 구분한 단위 : 토큰
    answer_out = [] # 디코더에 출력할 답변의 끝 , <END> 토큰(단어)를 문장 끝에 추가

    #질의에 대한 전처리
    for text in texts :
        question = clean_and_morph(text,is_question=True) # is_question=True 질의
        questions.append(question)  # 질문을 질문 목록에 담는다.

    #답변에 대한 처리
    for pair in pairs :
    #전처리와 morph 수행 #처리하기 쉬운형태로 변경
        in_,out_ = clean_and_morph(pair,is_question=False)# , is_question= False 답변
        answer_in.append(in_) #답변시작 추가
        answer_out.append(out_) #답변종료 추가
    return questions, answer_in, answer_out # 질문전체리스트,답변시작,답변끝

# 전체 문자를 하나의 리스트로 만들기 #
questions,answer_in,answer_out = preprocess(texts,pairs)
print(questions[:2]) 
print(answer_in[:2])
print(answer_out[:2])

#전체 문장을 하나의 리스트로 만들기
all_sentences = questions + answer_in + answer_out

#라이브러리 불러오기
import numpy as np
import warnings
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#WARNING 무시  # 경고 무시
warnings.filterwarnings('ignore')

# - 단어 사전 만들기
    # filters='' : 토큰화 할때 특정 기호를 제거(필터) # 필터링 하지 안겠다는 뜻
    # lower = False : 토큰화 할때 소문자로 변환하지 여부 # 기본값 true 이므로 모든 영문을 소문자로 변환
        # false 이므로 변환하지 않는다.
    # oov_token : 단어 사전에 없는 단어를 매칭할때 그 단어를 대체할 문자<OOV> 표현

tokenizer = Tokenizer(filters="",lower=False,oov_token='<OOV>')
tokenizer.fit_on_texts(all_sentences)
print( tokenizer.word_index ) # 단어 사전 확인

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
# - 텐서플로의 Model 클래스로부터 상속받아 인코더 클래스 정의하기

# 상속 : 하나의 클래스가 다른 클래스에게 속성/필드 과 함수/기능 물려두는 행위
    # 자바 : class 클래스A extends 클래스B{ }
        # this , super
    # 파이썬 : class 클래스A( 클래스B ) :
        # self , super

#인코더
class Encoder(tf.keras.Model) :
    # 초기화함수 # 생성자 # 사용할 변수 , 레이어를 미리 불러와서 파라미터 값들을 미리 설정 한다.
    def __init__(self,units,vocab_size,embedding_dim,time_steps):

        # units 매개변수1 : LSTM에서 사용할 유닛/노드/뉴런 수
        # "안녕하세요, 오늘 날씨 어떄요?" 문장 가정이라고 했을때.
        # vocab_size 매개변수2 : 임베딩 레이어의 입력으로 들어가는 단어 크기
        # "안녕하세요" , "오늘" , "날씨" ,"어때요" => 4
        # embedding_dim 매개변수3 : 임베딩 레이어의 각 단어를 크기의 벡터 차원
        # 밀집행렬를 처리할때 한 단어를 표현을 차원수 # "안녕하세요" 몇차원으로 구성할지
        # time_steps 매개변수4 : 임베딩 레이어의 입력으로 들어가는 시퀀스의 길이
        # 한번에 몇개의 단어를 모델이 학습하고 기억할지 단위 길이 # 2 => "안녕하세요" , "오늘"

        super(Encoder,self).__init__() # 상속받은 슈퍼클래스의 초기화함수(생성자) 를 호출
        # 1. 임베딩 레이어
        self.embedding = Embedding(vocab_size,embedding_dim,input_length=time_steps)
        # 2. 드롭아웃 레이어 # 일반드롭아웃 # 0.2 : 20%를 무작위로 비활성
        self.dropout = Dropout(0.2)
        # 3. LSTM 레이어 #
        self.lstm = LSTM(units,return_state = True)
        
    # 실행 함수
    def call(self,inputs):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x,hidden_sate,cell_sate = self.lstm(x)
            # x : LSTM 알고리즘이 특정 단어로 부터의 특징(정보/패턴) 값
                # 문장 : '오늘 무엇을 먹을까?' ---> 현재 문장의 분석 결과를 알려주는 출력값
            # 은닉 상태 : LSTM 알고리즘이 현재 시점에서의 기록한 특징들(정보/패턴)들을 저장하는 메모리
                # L(LONG)S(SHORT)T(TERM)M : 앞전 문장을 잊지 않고 지속하는 문장을 기록하는 메모리
            # 셀 상태 : LSTM 알고즘이 전체 단어들 에서 중요한 특징(정보/패턴)들을 저장하는 메모리
                # 앞전 전체 분석된 문장들 중에서 중요한 단어들을 기억하는 메모리
            # (특징/패턴) 분석
                # CNN : 이미지 분석 , # 곡선 , 색감 , 사이즈 , 비율 , 질감(텍스처) 등등 # 0~255 # 컴퓨터는 이미지를 RGB
                # RNN : 텍스트 분석 , # 빈도 , 감정 , 형태소(동사,형용사 등등) , 단어의 의미 # 벡터 # 컴퓨터는 텍스트 대신 벡터
        # Dense 레이어가 없는 이유는 현재 클래스(인코더) 의 목적은 입력과정 하기 위해서 --> 디코더 전달할 예정
        return [hidden_sate,cell_sate]

# 디코더
# - 텐서플로의 Model 클래스로부터 상속받아 디코더 클래스 정의하기
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
        # return_state=True : 생략가능(기본값) , 은닉상태와셀상태 반환 설정
        # return_sequences=True : 모든 시점의 출력을 반환한다.
        # initial_state : 초기화상태 속성 # 인코더와 결합 이후에 인코더에 생성한 은닉상태 와 셀 상태를 대입한다.
        x = self.dense(x)
        return x, hidden_sate,cell_state

    #day39 복사 > day41붙여넣기 p-329
# ===================================================================
# 모델 결합
class Seq2Seq(tf.keras.Model) : #클래스 정의
    #1. 초기화 함수 #개겣 생성자 함수
    def __init__(self,units,vocab_size,embedding_dim,time_steps,start_token,end_token):
        super(Seq2Seq,self).__init__()
        self.start_token = start_token #객체의 속성을 정의 후 매개변수 대입 #시작 토큰 # 모델이 문장을 생성할 때 시작을 식별하기 위해 사용
        self.end_token = end_token  #객체의 속성을 정의 후 매개변수 대입 #끝 토큰 # 모델이 문장을 생성할 때 끝마침을 식별하기 위해 사용
        self.time_steps = time_steps
        #
        self.encoder = Encoder(units,vocab_size,embedding_dim,time_steps) #인코더 객체 생성 # 각 매개변수 대입
        self.decoder = Decoder(units,vocab_size,embedding_dim,time_steps) #디코더 객체 생성 # 각 매개변수 대입

    #2. 실행 함수 # 객체 호출 함수
    def call(self,inputs,training=True):
        #inputs : 모델 객체 안으로 들어오는 입력 데이터
        #training = True : #ture 훈련중 일때, false : 훈련중이 아닐때 = 매개변수 = 초기값 # 훈련 중을 기본값으로 사용중
        if training : #만약에 훈련중이면
            encoder_inputs, decoder_inputs = inputs # 현재 모델이 주어진 인코더와 디코더의 입력 #fit() 메소드 호출시 들어오는 데이터
            context_vector = self.encoder(encoder_inputs) #인코더 객체의 실행 결과를 받는다. #encoder 객체의 call함수를 실행
            decoder_outputs,_,_ = self.decoder(inputs=decoder_inputs,initial_state = context_vector)
            #decoder 객체의 call 함수 호출 하고 결과 받기 #initial_sate : 인코더 결과 값
                #_(언더바) : 변수 생략 #for _ in 리스트 # (값 , _ , _) = 함수()
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

VOCAB_SIZE = len(tokenizer.word_index)+1 #tokenizer.word_index 단어사전 #단어사전개수 +1 oov 추가했으므로

# - 디코더의 결과를 원핫 인코딩 벡터로 변환
# 컴퓨터가 이해하는 언어인 벡터로 변환하는 방법
# 임베딩(밀집행렬) : 주로 챗봇의 질문에서 사용된다. (학습 데이터) # 임베딩은 단어 간의 유사성 파악 유리
# vs
# 원핫인코딩 : 주로 챗봇의 답변에서 사용된다 . (결과 데이터) # 유사성 파악 아닌 단순 분류 에서 유리

#모델이 예측한 단어목록(indexs : 예측한단어의 인덱스)
def convert_to_one_hot(padded) :
    # 1. 응답 개수 만큼의 차원수를 0으로 채우기
    one_hot_vector = np.zeros((len(answer_out_padded),MAX_LENGTH,VOCAB_SIZE)) #:np.zeros() # 지정한 차원수만큼 0 으로 채워짐
    # (데이터1,데이터2,데이터3) : 3차원 배열치고화 
    # len(answer_out_padded) : 총 응답 개수
    # Max_LENTH : 문장내 최대 길이
    # VOCAB_SIZE : 단어 사전의 단어수
    # (응답단어의 총개수 최대 길이 단어사전의 수)
    
    # 2. 전체 0으로 채우고 지정된 곳에 1을 넣어주는 방식 (단어 사전에 존재하는 경우에 해당인덱스의 1 으로 채우기)
        #1. 행
    for i, sequence in enumerate(answer_out_padded): # for index , value in enumerate (리스트) : 
        #2. 열
        # i : 현재 시퀀스의 인덱스 # sequence : 현재 시퀀스의 단어
        for j, index in enumerate(sequence):
            #3. 높이
            # j: 현재 단어의 인덱스 # 현재 단어의 인덱스 번호
            one_hot_vector[i,j,index] = 1

    return one_hot_vector

    #.zeros(차원수) : 지정한 차원수 만큼 0 으로 채워진다.
    # 1.(np).zeros(5) : [0 0 0 0 0]
    # 2.(np).zeros(3,4) : [[0 0 0 0 ][0 0 0 0 ][0 0 0 0 ]]
    # 3.(np).zeros(2,3,4) : [[0 0 0 0 ][0 0 0 0 ][0 0 0 0 ]], [[0 0 0 0 ][0 0 0 0 ][0 0 0 0 ]]

answer_in_one_hot = convert_to_one_hot(answer_in_padded)
answer_out_one_hot = convert_to_one_hot(answer_out_padded)
print(answer_in_one_hot[0].shape)
print(answer_out_one_hot[0].shape)

def convert_index_to_text(indexs,end_token): 
    sentence = " " # 생성된 문장을 저장할 변수를 선언 # 처음에는 빈 문자열
    #

    for index in indexs: #index 배열의 각 인덱스를 반복 # 해당 배열에는 예측된 단어가 위치한 배열
        if index == end_token : #만약에 현재 인덱스가 end_token(마지막 문장) 이면 문장 생성을 중단한다.
            break;
        # 예측한 인덱스가 0보다 크고 (토큰나이저) 단어사전내 지정한 인덱스의 단어가 None이 아니면 
        if index > 0 and tokenizer.index_word[index] is not None: #단어사전에 none 이 아니면
            sentence += tokenizer.index_word[index] # 찾았으면 찾은 단어를 생성한 문장 변수에 += 누적으로 더한다.
        else : #단어 사전에 없는 인덱스 이면 빈 문자열 추가
            sentence += ""
            # 빈칸 추가 # 다음 반복으로(다음 단어 생성) 이동 하기 전에 띄어쓰기 추가
        sentence += " " #공백 추가
        # 전체 반복문이 종료
    return  sentence #생성된 문장(변수) 반환

#모댈 객체 생성 하기전에 파라미터 값 추가
BUFFER_SIZE = 1000 #버퍼 : 훈련 중에 저장할 (무작위) 샘플 최대수
# 버퍼가 클수록 다양하게 잘 섞여서 학습에 성능 향상 하는데, 메모리 소모가 크다. # 조절 
BATCH_SIZE = 16 #배치 : 모델이 훈련 중에 훈련 1번에 있어서 사용할 사용되는 샘플 수 
# 배치가 클수록 안정적이지만, 메모리 소모가 크다 #8,16,32 단위로 주로 사용된다. # 조절
EMBEDDING_DIM = 100 #임베딩 차원 : 단어를 벡터로 인코딩 과정, 인코딩 과정에 있어서 한 단어가 사용할 차원수
# 벡터로 표현할 차원수가 크면 표현 성능이 좋아지지만 # 메모리 소모 와 계산비용이(계산속도) 증가한다. #단어들간의 의미 관계를 파악할수 있다.
TIME_STEPS = MAX_LENGTH #단어의 최대길이 #문장내 단어의 최대 개수 #30(임의)
START_TOKEN = tokenizer.word_index['<START>'] #문장의 시작을 알리는 토큰(단어) 인덱스 # 단어 생성시(예측) 시작 위치
END_TOKEN = tokenizer.word_index['<END>'] #문장의 끝을 알리는 토큰(단어) 인덱스 # 단어 생성시(예측) 해당 토큰을 만나면 문장 생성(예측) 종료

UNITS = 128 #유닛 수 : RNN(유닛),CNN(노드) => 뉴런 수 # 각 모델이 학습하는 레이어에 사용될 뉴런 수
# 많은 유닛 수를 사용하면 더 복잡한 학습이 가능하지만, 과대적합에 빠질 수 있다, 주로 32,64,128 단위로 사용된다.
VOCAB_SIZE = len(tokenizer.word_index) +1 #미리만든 단어사전의 단어수 +1 (+1 : <OOV> 때문에 추가)
NUM_EPOCHS = 20 # 훈련 횟수

DATA_LENGTH = len(questions) #질문의 총 개수
SAMPLE_SIZE = 3 # 샘플 개수

#모델의 가중치를 저장하고 추후에 가중치를 재 호출하여 다른 모델 또는 곳 에서 재 사용
# ckpt --> .weights.h5 # 가중치 저장 (ckpt : 옛날거)
checkpoint_path = 'model/seq2seq-chatbot-checkpoint.weights.h5' #경로/파일명.weight.h5 (모델 가중치 저장) # model 이라는 폴더 생성
from tensorflow.keras.callbacks import ModelCheckpoint #체크포인트 클래스 모듈 가져오기(호출)
checkpoint = ModelCheckpoint(filepath=checkpoint_path, #모델 가중치를 저장할 파일 경로 지정
                             save_weights_only=True, # 모델의 가중치만 저장 #True 모델의 구조는 저장되지 않는다. #False : 구조 저장 , True : 가중치만 저장
                             save_best_only=True, # 훈련중 모니터 (fit:var_loss) 값이 개선될때 만 가중치를 저장 #성능이 향상될 때 체크포인트 업데이트
                             monitor='loss', # 어떤 값을 모니터링 할지 지정 # loss(손실함수) 손실함수가 발생시?
                             verbose=1) # 과정로그 수준 # 생략가능

#seq2seq

#시퀀스 모델 객체 생성
seq2seq = Seq2Seq(UNITS,VOCAB_SIZE,EMBEDDING_DIM,TIME_STEPS,START_TOKEN,END_TOKEN)
#모델 컴파일
seq2seq.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

#모델 학습 후 예측 함수
def make_prediction(model,question_inputs): # model : 학습한 모델 , question_inputs : 예측할 새로운 질문
    results = model(inputs=question_inputs, training=False) #예측이므로 훈련이 아니다. #Seq2Seq클래스내 call함수내 else 코드들이 실행된다.
    results = np.asarray(results).reshape(-1) # 변환된 인덱스를 문장으로 변환
    # 예측된 결과를 np(넘파이) 배열로 변환 하고 차원을 1차원(-1) 배열로 변경한다. #나중에 문장 조회시 평탄화(1차원변경)하고 convert_indext_to_text() 에게 전달할 예정
    return results

for epoch in range(NUM_EPOCHS) : #총 20회 반복하기
    print(f'processing epoch : {epoch * 10 + 1}...') #현재 에포크 진행률 
    seq2seq.fit([question_padded,answer_in_padded], #모델 피팅
                    answer_out_one_hot,#원핫 인코딩
                    epochs= 10, #10회 > 총200회
                    batch_size=BATCH_SIZE,
                    callbacks=[checkpoint]
                #fit() : 모델 훈련 함수
                #1. [question_padded,answer_in_padded] : 입력 데이터
                #2. answer_out_one_hot : 결과 데이터
                #3. callbacks : 훈련중 체크포인트를 지정한다. #가중치만저장
                )
    # 훈련후 샘플 수 만큼 난수의 질문을 이용하여 성능 예측하기
    samples = np.random.randint(DATA_LENGTH,size=SAMPLE_SIZE) #전체 질문에서 3개의 질문을 난수로 추출

    #예측 성능 테스트
    for idx in samples: # 임의의 3개의 질문이 있는 리스트
        question_inputs = question_padded[idx] #선정된 질문의 인코딩된 단어를 가져오기
        # 예측 #np.expand_dims(배열,0) : 새로운 차원 추가 # 0 : 첫번째 자리에 차원추가
        #(1, 단어의 패딩 값) : 2차원 배열 만든다. # 모델의 예측 매개변수가 2차원이라서 차원 맞추기 (응답차원=0,입력차워)
        results = make_prediction(seq2seq, np.expand_dims(question_inputs,0))
        #예측한 벡터(숫자)들을 문장으로 변환
        results = convert_index_to_text(results,END_TOKEN)
        #확인
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
    

