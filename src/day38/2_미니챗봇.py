#2_미니챗봇.py
import re
from cgi import maxlen

import numpy as np
import pandas as pd

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
outputs_sequences = np.array(outputs)

#1. 모델

#2. 컴파일

#3. 학습