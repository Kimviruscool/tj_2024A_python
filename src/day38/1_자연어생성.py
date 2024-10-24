#day40 자연어생성

import tensorflow as tf
import pandas as pd
from unicodedata import bidirectional

#1. 데이터 수집 #get.file()
file = tf.keras.utils.get_file(
    'reting_train.txt', #설정할 파일명
    origin = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt', #다운로드 받을 링크
    extract= True #압축 설정
)

df = pd.read_csv(file,sep='\t')
print(df[1000:1007]) #데이터 중 임의의 행 확인

#형태소 분석기
from konlpy.tag import Okt
okt = Okt()

#데이터 전처리
def word_tokenization(text):
    return [word for word in okt.morphs(text)]

def preprocessing(df):
    df = df.dropna()
    df = df[1000:2000] #샘플 데이터 1000개 학습 시간을 줄이고자 함
    df['document'] = df['document'].str.replace("[^A-Za-z0-9가-힣ㄱ-ㅎㅏ-ㅣ]","")
    data = df['document'].apply((lambda x:word_tokenization(x)))
    return data

review = preprocessing(df)
print(len(review))
#1000

#분리된 형태소 데이터 확인
print(review[:10])
'''
1000    [정말, 최고, 의, 명작, 성인, 이, 되고, 본, 이집트, 의, 왕자, 는, 또...
1001    [이영화, 만, 성공, 했어도, 스퀘어, 가, 에, 닉스, 랑, 합병, 할, 일, ...
1002                                 [울컥, 하는, 사회, 현실, ㅠㅠ]
1003       [기대, 를, 하나, 도안, 하, 면, 할, 일, 없을, 때, 보기, 좋은, 영화]
1004    [소림사, 관문, 통과, 하기, 진짜, 어렵다는거, 보여준, 영화, .., 극장, ...
1005                              [시리즈, 안, 나오나, ㅠㅠㅠㅠㅠㅠㅠㅠ]
1006    [끝난다는, 사실, 이, 너무, 슬퍼요, ., 가슴, 이, 뻥, 뚫려, 버린것, 같...
1007                                             [펑점, 조절]
1008                   [와, .., 이건, 진짜, 으리, 으리, 한, 데, ..?]
1009            [손발, 이, 오, 그라드, 네, 요, ..................]
Name: document, dtype: object
'''

#토큰화 및 패딩
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer()

def get_tokens(review):
    tokenizer.fit_on_texts(review)
    total_words = len(tokenizer.word_index)+1
    tokenized_sentences = tokenizer.texts_to_sequences(review)

    input_sequences = []
    for token in tokenized_sentences:
        for t in range(1, len(token)):
            n_gram_sequence = token[:t+1]
            input_sequences.append(n_gram_sequence)

    return input_sequences, total_words

input_sequences, total_words = get_tokens(review)
input_sequences[31:40]

#단어 사전
print("감동 :",tokenizer.word_index['감동'])
print("영화 :",tokenizer.word_index['영화'])
print("영화 :",tokenizer.word_index['코믹'])

#문장 길이 동일하게 맞추기

import numpy as np

max_len = max([len(word) for word in input_sequences])
print("max_len : ", max_len)
input_sequences = np.array(pad_sequences(input_sequences,maxlen=max_len,padding='pre'))

#입력 텍스트와 타깃

from tensorflow.keras.utils import to_categorical
x = input_sequences[:,:-1],
y = to_categorical(input_sequences[:,-1],num_classes=total_words)

#y를 설명하기 위한 예시
a = to_categorical([0,1,2,3], num_classes=4)
print(a)

#모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense,Bidirectional,Dropout

embedding_dim = 256

model = Sequential([ #딥러닝 모델
    #임베딩 레이어
    Embedding(input_dim=total_words,
              output_dim=embedding_dim,
              input_length=max_len-1),
    Bidirectional(LSTM(units=256)),
    Dense(units=total_words,activation='softmax') #다중분류이므로 활성화 함수는 softmax
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x,y,epochs=20)

def text_generation(sos, count):
    for _ in range(1, count):
        token_list = tokenizer.texts_to_sequences([sos])[0]
        token_list = pad_sequences([token_list],maxlen=max_len-1,padding='pre')
        predicted = np.argmax(model.predict(token_list),axis=1)

        for word,idx in tokenizer.word_index.items():
            if idx == predicted :
                #만약에 단어 사전내 인덱스가 예측 인덱스와 같으면
                output = word #찾은 인덱스의 단어 저장
                break
        sos += " " + output #새로운 문장 뒤에 예측한 단어 연결하기
    return sos

# data = [[0.1,0.2,0.7],[0.3,0.5,0.2],[0.4,0.3,0.3]]
# np.argmax([data],axis=-1)

print(text_generation("연애 하면서",12))
print(text_generation("꿀잼",12))
print(text_generation("최고의 영화",12))
print(text_generation("손발 이",12))

