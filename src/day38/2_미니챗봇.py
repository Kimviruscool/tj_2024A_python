#2_미니챗봇.py
from cgi import maxlen

import numpy as np
import pandas as pd
from tensorflow.python.ops.numpy_ops import result_type

#RNN 기본구조 : 1. 데이터수집 2. 데이터전처리 3.토큰화/패딩 4.모델구축 5.모델학습 6.모델평가(튜닝) 7.모델예측

#데이터 수집
data = [
    {"user": "안녕하세요", "bot": "안녕하세요! 무엇을 도와드릴까요?"},
    {"user": "오늘 날씨 어때요?", "bot": "오늘은 맑고 화창한 날씨입니다."},
    {"user": "지금 몇 시에요?", "bot": "현재 시간은 오후 3시입니다."},
    {"user": "좋은 책 추천해 주세요", "bot": "최근에 인기가 많은 책은 '파이썬 데이터 분석'입니다."},
    {"user": "고마워요", "bot": "천만에요! 더 필요한 것이 있으면 말씀해주세요."}
]

data = pd.DataFrame(data) #데이터 프레임 변환

# 데이터 전처리
inputs = list(data['user']) #질문
outputs = list(data['bot']) #응답
import re

from konlpy.tag import Okt
okt = Okt()
def preprocess(text):
    # 한글과 띄어쓰기를 제외한 문자 제거 #^반대
    result = re.sub(r'[^가-힣\s]','',text) #정규표현식 #일반적인 문자열 정규표현식
    # 형태소 분석
    result = okt.pos(result) #[ ('라면','Noun),('먹다',Verb) ]
    # 명사와 동사 와 형용사 외 제거 #형태소 분석기가 각 형태소들을 명칭하는 단어들 (pos)변수에 존재한다.
    result = [word for word, pos in result if pos in ['Noun','Verb','Adjective'] ] #Noun : 명사, Verb: 동사 , Adjective : 형용사
    # 불용어 생략
    # 반환
    return " ".join(result).strip() #strip() : 앞뒤 공백 제거 함수

# 전처리 실행
preprocess_inputs = [preprocess(질문) for 질문 in inputs]
print(preprocess_inputs)
#['안녕하세요', '오늘 날씨 어때요', '지금 몇 시', '좋은 책 추천 해 주세요', '고마워요']

#3.토크나이저
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocess_inputs) #전처리된 단어 목록을 단어사전 생성
print(tokenizer.word_index) #사전확인

#패딩
input_sequences = tokenizer.texts_to_sequences(preprocess_inputs) #백터화

max_sequence_length = max(len(문장) for 문장 in input_sequences ) #가장 긴 길이의 문장 개수

input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length) #패딩화

#종속변수 #데이터프레임 > 일반 배열 반환
outputs_sequences = np.array(range(len(outputs)))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM, Dense, Bidirectional

#1. 모델
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index), output_dim= 50, input_length=max_sequence_length))
model.add(Bidirectional(LSTM(256))) # 256,128,64,32
model.add(Dense(len(outputs), activation='softmax')) #종속 변수의 값 개수는 응답 개수

#2. 컴파일
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#3. 학습
model.fit(input_sequences, outputs_sequences, epochs=10)

#4. 예측하기
def response(text) :
    # 1. 예측할 값도 전처리 한다.
    text = preprocess(text)
    print(text)
    # 2. 예측할 값도 토큰 과 패딩
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text , maxlen=max_sequence_length)
    # 3. 예측
    result = model.predict(text)
    # 4. 결과 가장 높은 확률의 인덱스 찾기
    max_idx = np.argmax(result)
    # 5.
    return outputs[max_idx]

# 확인
print(response('안녕하세요')) #질문이 안녕하세요

# 서비스 제공한다. #플라스크
while True :
    text = input('사용자 : ') #챗봇에게 전달할 내용 입력받기
    result = response(text) #입력받은 내용을 함수에 넣어 예측을 한다.
    print(f'챗봇 : {result}') # 예측한 응답 출력한다.