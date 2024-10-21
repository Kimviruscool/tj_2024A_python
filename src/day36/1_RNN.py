# day36 - 1_RNN.py
import tensorflow as tf


#1. 임베딩 레리어 구현 # Embedding(): 입베딩 클래스 String
embedding_layer = tf.keras.layers.Embedding(100,3) #100개 단어, 3차원 차원
result = embedding_layer(tf.constant([12,8,15,20])) #임의(더미)의 숫자 4개를 입력데이터를 넣어준다.
print(result) # 각 임의의 데이터 4개를 임베딩 레이어를 걸쳐 3개 숫자로 변환하여 표현된다.
'''
tf.Tensor(
[[-0.01233163  0.03129138 -0.02310146] 12 데이터
 [ 0.02297742  0.03155203  0.04583151] 8 데이터 
 [-0.01367464  0.00498777  0.01622492] 15 데이터
 [ 0.03206182 -0.04175894 -0.0418401 ] 20 데이터
 ] , shape=(4, 3), dtype=float32)
 결론 : 각 숫자(단어)를 의미 하는 벡터로 바꾸어 주는 임베딩 레이어 역할
'''
#임베딩 레이어 활용
model = tf.keras.Sequential()
#100개의 단어를 3차원 벡터로 변환하겠다는 속성값 대입, 최대 32개의 단어로 이루어져 있다는 속성값 대입
model.add(tf.keras.layers.Embedding(100,3,input_length=32)) #.add(레이어객체) : 레이어추가
#32개의 결과를 예측한다.
model.add(tf.keras.layers.LSTM(units=32)) #Long short Term Memory : 긴 문장에서 중요한 정보는 기억하는 RNN 클래스
#출력(결과) 레이어 
model.add(tf.keras.layers.Dense(units=1)) #
print(model.summary())
'''
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding_1 (Embedding)     (None, 32, 3)             300       
                                                                 
 lstm (LSTM)                 (None, 32)                4608      
                                                                 
 dense (Dense)               (None, 1)                 33        
                                                                 
=================================================================
Total params: 4,941
Trainable params: 4,941
Non-trainable params: 0

'''
#라이브러리 불러오기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense

model = Sequential()
model.add(Embedding(100,3,input_length=32))
model.add(LSTM(32))
model.add(Dense(1))
model.summary()

#Bidirectional LSTM
from tensorflow.keras.layers import Bidirectional

model = Sequential()
model.add(Embedding(100,3)) #임베딩 (총 단어수 : 100 차원수: 3) #매개변수의 수 : 100*3 = 300
model.add(Bidirectional(LSTM(32))) #LSTM 구조를 양방향으로 설정 유닛 개수가 32개 2배인 64개 나왔다.
model.add(Dense(1))
model.summary()

#스태킹 RNN 예제 (여러개 RNN 쌓기 (여러개 모델))
model = Sequential() 
model.add(Embedding(100,32)) #총 100개의 단어 32차원
model.add(LSTM(32,return_sequences=True)) # 32개의 유닛(뉴런) #모든 timeStep에 대해 출력을 한다.
model.add(LSTM(32)) #최상단 RNN 에서는 return_sequences = True 할 필요가 없다.
model.add(Dense(1)) #출력 레이어
model.summary()
'''
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding_4 (Embedding)     (None, None, 32)          3200      
                                                                 
 lstm_3 (LSTM)               (None, None, 32)          8320      
                                                                 
 lstm_4 (LSTM)               (None, 32)                8320      
                                                                 
 dense_3 (Dense)             (None, 1)                 33        
                                                                 
=================================================================
Total params: 19,873
Trainable params: 19,873
Non-trainable params: 0
_________________________________________________________________
'''

# 순환 드롭아웃
model = Sequential()
model.add(Embedding(100,32))
    # recurrent_dropout=0.2 # LSTM의 순환 드롭아웃의 비율
        # 타임스탭의 출력을 다음 타임스탭의 입력으로 20%를 무작위로 제거하여 과대 적합을 방지한다.
    # dropout=0.2
        # 입력으로 들어오는 데이터으로 사용할때 20%를 무작위로 제거 하여 과대 적합을 방지한다.
model.add(LSTM(32,recurrent_dropout=0.2,dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.summary()
