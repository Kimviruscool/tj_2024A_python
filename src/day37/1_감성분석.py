#1_감성분석 #python3.8.ver

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import warnings

from numpy.array_api import trunc

warnings.filterwarnings(action='ignore')

#데이터 불러오기
train_file = tf.keras.utils.get_file(
    'rating_train.txt',
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt', extract=True)
train = pd.read_csv(train_file,sep='\t')

#EDA탐색적 데이터분석

#데이터 크기 및 샘플 확인
print("train shape : ", train.shape) #크기
print(train.head()) #샘플 상위 5개

#레이블별 개수
#pd객체['필드명'].value_counts() : 지정한 필드의 데이터별 개수
cnt = train['label'].value_counts()
print(cnt)

#레이블별 비율 시각화
sns.countplot(x='label',data=train)
# 0    75173 #부정
# 1    74827 #긍정

#결측지 확인
print(train.isnull().sum())

#결측지(의견없음)가 특정 label 값만 있는지 확인
print(train[train['document'].isnull()])

#레이블별 텍스트 길이
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
data_len = train[train['label']==1]['document'].str.len()
ax1.hist(data_len)
ax1.set_title('positive')

data_len = train[train['label']==1]['document'].str.len()
ax2.hist(data_len)
ax2.set_title('negative')
fig.suptitle('Number of characters')
plt.show()

#Mecab 형태소 설치생략

#형태소 분석기 객체 불러오기
from konlpy.tag import Kkma,Komoran,Okt,Mecab
kkama = Kkma()
komoran = Komoran()
okt = Okt()
mecab = Mecab

#형태소별 샘플
text = "영실아안녕오늘날씨어때?"

def sample_ko_pos(text):
    print(f'========={text}==========')
    print("kkma : ",kkama.pos(text))
    print("komoran : ", komoran.pos(text))
    print("okt : ", okt.pos(text))
    print("\n")

sample_ko_pos(text)

text2 = "영실아안뇽오늘날씨어때?"
sample_ko_pos(text2)

text3 = "정말 재미있고 매력적인 영화에요 추천합니다."
sample_ko_pos(text3)

#데이터 전처리
train['document'] = train['document'].str.replace("[A-za-z가-힣ㄱ-ㅎㅏ-ㅣ]","")
print(train['document'].head())

#결측치 제거
train = train.dropna()
print(train.shape)

#스탑워드와 형태소 분석 (한글 불용어)
def word_tokenization(text) :
    stop_words = ["는","을","를","이","가","의","던",'고','하','다','은','에','들','지','게','도']
    return [word for word in okt.morphs(text) if word not in stop_words]

data = train['document'].apply((lambda x:word_tokenization(x)))
print(data.head())

#train과 validatation 분할
training_size = 120000
#train 분할
train_sentences = data[:training_size]
valid_sentences = data[training_size:]
# label 분할
train_labels = train['label'][:training_size]
valid_labels = train['label'][training_size:]

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#vocab_size 설정
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data)
print("총 단어 개수 :",len(tokenizer.word_index))
#5회 이상만 vocab_size에 포함
def get_vocab_size(threshold):
    cnt = 0
    for x in tokenizer.word_counts.values():
        if x >= threshold:
            cnt = cnt+1
    return cnt

vocab_size = get_vocab_size(5)
print("vocab_size : ", vocab_size)

oov_tok = "<OOV>" #사전에 없는 단어는 "<OOV>" 로 표현
vocab_size = 15000

#단어 사전 만들기
tokenizer = Tokenizer(oov_token=oov_tok, num_words=vocab_size+1)
tokenizer.fit_on_texts(data)
print(tokenizer.word_index)
print("단어 사전 개수 : ", len(tokenizer.word_counts))

#문자를 숫자로 표현
print(train_sentences[:2])
train_sequences = tokenizer.texts_to_sequences(train_sentences)
valid_sequences = tokenizer.texts_to_sequences(valid_sentences)
print(train_sequences[:2])

#문장의 최대 길이
max_length = max(len(x) for x in train_sequences)
print("문장 최대 길이 : ", max_length)

#문장 길이를 동일하게 맞춘다.
trunc_type = 'post'
padding_type = 'post'

train_padded = pad_sequences(train_sequences,
                             truncating=trunc_type,
                             padding=padding_type,
                             maxlen=max_length)
valid_padded = pad_sequences(valid_sequences,
                             truncating=trunc_type,
                             padding=padding_type,
                             maxlen=max_length)
train_labels = np.asarray(train_labels) #배열로변환
valid_labels = np.asarray(valid_labels)

print("샘플 : ",train_padded[:1])

#모델
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,LSTM,Embedding,Bidirectional

def create_model():
    model = Sequential([
        Embedding(vocab_size,32),
        Bidirectional(LSTM(32,return_sequences=False)),
        Dense(32,activation='relu'),
        Dense(1,activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

model = create_model()
model.summary()

# 가장 좋은 loss의 가중치 저장
checkpoint_path = 'best_performed_model.ckpt'
checkpoint = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                save_weights_only=True,
                                                save_best_only=True,
                                                monitor='val_loss',
                                                verbose=1)

#학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=2)

#학습
history = model.fit(train_padded,train_labels,
                    validation_data=(valid_padded,valid_labels),
                    # callbacks=[early_stop,checkpoint],
                    batch_size=64, epochs=10, verbose=2)
#verbose 학습시 콘솔에 요약정도 0: 출력없음 1: 진행률바 2:결과요약만

print(history) #최종정확도 손실함수 확인

#새로운 리뷰 텍스트의 감정 분석 하기 #예측하기
new_reviews = ['영화 정말 재미있다','정말 지루하다','그냥 보통 이었어요.','생각보다 재미가 없다']
#새로운 리뷰도 전처리
new_sequences = tokenizer.texts_to_sequences(new_reviews) #.texts_to_sequences
new_padded_sequences = pad_sequences(new_sequences,maxlen=max_length)
#모델 이용한 감성 예측
result = model.predict(new_padded_sequences)
#예측 결과
for index, review in enumerate(new_reviews) : #for 인덱스,반복변수 in enumerate(반복할객체)
    print(f'리뷰 : {review}, 확률 : {result[index]}')
'''
리뷰 : 영화 정말 재미있다, 확률 : [0.5188895]
리뷰 : 정말 지루하다, 확률 : [0.50937414]
리뷰 : 그냥 보통 이었어요., 확률 : [0.5325484]
리뷰 : 생각보다 재미가 없다, 확률 : [0.50728726]
'''