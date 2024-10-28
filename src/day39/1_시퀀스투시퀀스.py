# 1_시퀀스투시퀀스

import pandas as pd
from fontTools.misc.cython import returns
from joblib.numpy_pickle_utils import BUFFER_SIZE
from keras.integration_test.preprocessing_test_utils import VOCAB_SIZE, BATCH_SIZE
from numpy.ma.core import count
from promise.promise import MAX_LENGTH
from tensorflow.python.keras.utils.version_utils import training

# 1. 데이터수집
# 질문과 답변이 잇는 말뭉치를 가져오기
# Q질문 A답변 label(0일상다반사,1부정,2긍정)
corpus = pd.read_csv('https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv')
# 확인
print(corpus['Q'].head())  # 질문 열 의 상단 5개
print(corpus['A'].head())  # 답변 열 의 상단 5개
# 확인
print(f"Q : {corpus['Q'][0]}")
print(f"A : {corpus['A'][0]}")
# 확인
print(corpus.shape)  # 차원확인
# 샘플링(1000개사용)
texts = []  # 질문 리스트
pairs = []  # 답변 리스트

# for index , value in enumerate( 리스트/튜플 ) :
# for value in 리스트/튜플 :
print(zip(corpus['Q'], corpus['A']))

for i, (text, pair) in enumerate(zip(corpus['Q'], corpus['A'])):  # enumerate : 내장함수 #인덱스와 값을 동시에 접근하면서 반복문을 실행하려고할 때
    texts.append(text)
    pairs.append(pair)
    if i >= 1000:  # RAM문제로 1000개만
        break

# print(list(zip(texts,pairs))[1995:2000])

import re


def clean_sentence(sentence):  # 한글 , 숫자를 제외한 문자는 제거
    # 한글 , 숫자를 제외한 모든 문자는 제거
    # 1. re.sub(r'정규표현식', r'대체할문자' , 문자열 ) : 파이썬 내장용 문자열 정규표현식 함수
    # 2. pd['열이름'].str.replace("정규표현식","" , regex=True ) : 데이터프레임내 정규표현식 방법
    sentence = re.sub(r'[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\t]', " ", sentence)
    return sentence


print(clean_sentence("안녕하세요~:)"))  # 안녕하세요
print(clean_sentence("텐서플로!@#!$@!$"))  # 텐서플로

# 한글 형태소 분석
from konlpy.tag import Okt

okt = Okt()  # 형태소 분석 객체 생성


def process_morph(sentence):
    return ' '.join(okt.morphs(sentence))  # 형태소 분석 결과 목록 을 하나의 문자열 합치기
    # 형태소들 사이에 공백' ' 으로 구성한 문자열


print('안녕하세요'.join(['유재석', '강호동']))  # '유재석안녕하세요강호동'


# 한글 문장 전처리
# - 전처리 실행후 질문전체 , 답변시작 , 답변끝 구분
def clean_and_morph(sentence, is_question=True):  # 매개변수명=초기값 : 매개변수에 초기값 넣기
    # 한글 문장 전처리
    sentence = clean_sentence(sentence)
    # 형태소 변환
    sentence = process_morph(sentence)
    # 질문인 경우, 답인 경우를 분기하여 처리
    # 질문(Question) 인 경우 , Answer(답변) 인 경우를 구분하여 처리
    if is_question:
        return sentence
    else:  # 프로그래밍 언어에서 함수는 무조건 리턴(결과) 1개 이다.
        return (f'<START>  {sentence}', f'{sentence}  <END>')  # ( 값1 , 값2 ) : 튜플 형식 # ( )생략 가능


# - 질문전체 , 답변시작 , 답변끝 리스트 만들기
def preprocess(texts, pairs):
    questions = []  # 인코더에 입력할 질문 전체 리스트
    answer_in = []  # 디코더에 입력할 답변의 시작 , <START> 토큰을 문장 처음에 추가 , # 데이터들을 구분한 단위 : 토큰
    answer_out = []  # 디코더에 출력할 답변의 끝 , <END> 토큰(단어)를 문장 끝에 추가

    # 질의에 대한 전처리
    for text in texts:
        question = clean_and_morph(text, is_question=True)  # is_question=True 질의
        questions.append(question)  # 질문을 질문 목록에 담는다.

    # 답변에 대한 처리
    for pair in pairs:
        # 전처리와 morph 수행 #처리하기 쉬운형태로 변경
        in_, out_ = clean_and_morph(pair, is_question=False)  # , is_question= False 답변
        answer_in.append(in_)  # 답변시작 추가
        answer_out.append(out_)  # 답변종료 추가
    return questions, answer_in, answer_out  # 질문전체리스트,답변시작,답변끝


# 전체 문자를 하나의 리스트로 만들기 #
questions, answer_in, answer_out = preprocess(texts, pairs)
print(questions[:2])
print(answer_in[:2])
print(answer_out[:2])

# 전체 문장을 하나의 리스트로 만들기
all_sentences = questions + answer_in + answer_out

# 라이브러리 불러오기
import numpy as np
import warnings
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# WARNING 무시  # 경고 무시
warnings.filterwarnings('ignore')

# - 단어 사전 만들기
# filters='' : 토큰화 할때 특정 기호를 제거(필터) # 필터링 하지 안겠다는 뜻
# lower = False : 토큰화 할때 소문자로 변환하지 여부 # 기본값 true 이므로 모든 영문을 소문자로 변환
# false 이므로 변환하지 않는다.
# oov_token : 단어 사전에 없는 단어를 매칭할때 그 단어를 대체할 문자<OOV> 표현

tokenizer = Tokenizer(filters="", lower=False, oov_token='<OOV>')
tokenizer.fit_on_texts(all_sentences)
print(tokenizer.word_index)  # 단어 사전 확인

# 단어 사전 확인
for word, idx in tokenizer.word_index.items():
    print(f'{word}\t -> \t{idx}')
    if idx > 10:
        break

# 토큰 개수 확인
print(len(tokenizer.word_index))

# 치환 : 텍스트를 시퀀스로 인코딩(texts_TO_sequences)
question_sequence = tokenizer.texts_to_sequences(questions)
answer_in_sequence = tokenizer.texts_to_sequences(answer_in)
answer_out_sequence = tokenizer.texts_to_sequences(answer_out)

# 문장의 길이 맞추기(pad_sequences)
MAX_LENGTH = 30
question_padded = pad_sequences(question_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')
answer_in_padded = pad_sequences(answer_in_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')
answer_out_padded = pad_sequences(answer_out_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')

print(question_padded.shape)
print(answer_in_padded.shape)
print(answer_out_padded.shape)

from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint


# - 텐서플로의 Model 클래스로부터 상속받아 인코더 클래스 정의하기

# 상속 : 하나의 클래스가 다른 클래스에게 속성/필드 과 함수/기능 물려두는 행위
# 자바 : class 클래스A extends 클래스B{ }
# this , super
# 파이썬 : class 클래스A( 클래스B ) :
# self , super

# 인코더
class Encoder(tf.keras.Model):
    # 초기화함수 # 생성자 # 사용할 변수 , 레이어를 미리 불러와서 파라미터 값들을 미리 설정 한다.
    def __init__(self, units, vocab_size, embedding_dim, time_steps):
        # units 매개변수1 : LSTM에서 사용할 유닛/노드/뉴런 수
        # "안녕하세요, 오늘 날씨 어떄요?" 문장 가정이라고 했을때.
        # vocab_size 매개변수2 : 임베딩 레이어의 입력으로 들어가는 단어 크기
        # "안녕하세요" , "오늘" , "날씨" ,"어때요" => 4
        # embedding_dim 매개변수3 : 임베딩 레이어의 각 단어를 크기의 벡터 차원
        # 밀집행렬를 처리할때 한 단어를 표현을 차원수 # "안녕하세요" 몇차원으로 구성할지
        # time_steps 매개변수4 : 임베딩 레이어의 입력으로 들어가는 시퀀스의 길이
        # 한번에 몇개의 단어를 모델이 학습하고 기억할지 단위 길이 # 2 => "안녕하세요" , "오늘"

        super(Encoder, self).__init__()  # 상속받은 슈퍼클래스의 초기화함수(생성자) 를 호출
        # 1. 임베딩 레이어
        self.embedding = Embedding(vocab_size, embedding_dim, input_length=time_steps)
        # 2. 드롭아웃 레이어 # 일반드롭아웃 # 0.2 : 20%를 무작위로 비활성
        self.dropout = Dropout(0.2)
        # 3. LSTM 레이어 #
        self.lstm = LSTM(units, return_state=True)

    # 실행 함수
    def call(self, inputs):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x, hidden_sate, cell_sate = self.lstm(x)
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
        return [hidden_sate, cell_sate]


# 디코더
# - 텐서플로의 Model 클래스로부터 상속받아 디코더 클래스 정의하기
class Decoder(tf.keras.Model):
    def __init__(self, units, vocab_size, embedding_dim, time_steps):
        super(Decoder, self).__init__()
        self.embedding = Embedding(vocab_size, embedding_dim, input_length=time_steps)
        self.dropout = Dropout(0.2)
        self.lstm = LSTM(units, return_state=True, return_sequences=True)
        self.dense = Dense(vocab_size, activation='softmax')

    def call(self, inputs, initial_state):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x, hidden_sate, cell_state = self.lstm(x, initial_state=initial_state)
        # return_state=True : 생략가능(기본값) , 은닉상태와셀상태 반환 설정
        # return_sequences=True : 모든 시점의 출력을 반환한다.
        # initial_state : 초기화상태 속성 # 인코더와 결합 이후에 인코더에 생성한 은닉상태 와 셀 상태를 대입한다.
        x = self.dense(x)
        return x, hidden_sate, cell_state
