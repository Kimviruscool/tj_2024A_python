#2_단순싱경망 p66
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from jinja2.optimizer import optimize
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics
from tensorflow.python.ops.metrics_impl import mean_absolute_error

# #1. 임이의데이터 x 와 임이의 1차 함수
x = np.arange(1 , 6)
print(x) #[1,2,3,4,5]

y = 3 * x + 2
print(y) # [5 8 11 14 17]

# #2. 시각화
# plt.plot(x,y)
# plt.show()

#3. Sequential Api 모델 #여러 층을 이어 붙이듯 시퀀스에 맞게 일렬로 연결하는 방식 # 입력레이어/층 > 출력레이어/층 까지 순서를 갖는다.
#순서대로 각 층/레이어 를 하나씩 통과하면서 딥러닝 연산을 수행한다.

# #(1) 방법1 : 리스트형
# # model = tf.keras.Sequential([층1,층2,층3])
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(10), #레이어1
#     tf.keras.layers.Dense(5),#레이어2
#     tf.keras.layers.Dense(1) #레이어3
# ]) #Dense 레이어 3개를 갖는 모델 생성했다.
#
# #(2) 방법2 : add함수
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(10) )
# model.add(tf.keras.layers.Dense(5) )
# model.add(tf.keras.layers.Dense(1) )
# #tip : 레이어 개수는 제한이 없다.
#
# #(3) 입력 데이터의 형태
#
# model = tf.keras.Sequential([
#     # 데이터셋 (150, 4) # 150개의 데이터 #4개의 열(입력변수)
#     tf.keras.layers.Dense(1 , input_shaple=[4]), #레이어1 : 첫번째 레이어가 입력레이어 #반드시 input_shape 매개변수를 지정해야한다.
#     tf.keras.layers.Dense(5),#레이어2 :
#     tf.keras.layers.Dense(1) #레이어3
# ]) #Dense 레이어 3개를 갖는 모델 생성했다.

#(4) 단순 선형회귀 모델 정의 # y = wx + b 에서 데이터는 x 값을 나타내는 입력변수 1개만 존재하기 때문에 input_shape=[1]로 지정한다.
# 1개의 노드(뉴런)을 가지는 레이어는 1개의 출력 값을 가지므로 출력값은 y에 대한 모델의 예측값이다.
    #[1] 모델 생성
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape = [1])])
print(model.summary())
#total params : 2 # 모델 내부의 총 파라미터 수
# Trainable params: 2 (8.00 B) # 모델의 업데이트할 마라미터 수 # w가중치 , 편행b 두개이다.
#  Non-trainable params: 0 (0.00 B) #모델의 업데이트하지 않을 파라미터 수
    #[2] 컴파일
    #1. 긴 문자열 지정
model.compile(optimizer = 'sgd', loss = 'mean_squared_error', metrics = ['mean_squared_error','mean_absolute_error'])
    #2. 짧은 문자열 지정
model.compile(optimizer = 'sgd', loss = 'mse' , metrics = ['mse','mae'])
    #3. 클래스 인스턴스 지정
model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 0.005),
              loss = tf.keras.losses.MeanSquaredError(),
              metrics = [tf.keras.metrics.MeanAbsoluteError(), tf.keras.metrics.MeanSquaredError()])

# optimizer = 'sgd' : 확률적 경사하강법 알고리즘
#단순선형회귀 모델
model.compile(optimizer = 'sgd', loss = 'mse', metrics = ['mae'])
    #[3] 훈련
history = model.fit(x,y,epochs = 1200 ) #5번 반복 훈련 #1200번 반복 훈련
print(history)
    #[4] 시각화
plt.plot(history.history['loss'])
plt.plot(history.history['mae'])
plt.show()
    #[5] 검증
print(model.evaluate(x,y))
    #[6] 예측
print(model.predict(np.array( [10] ) ) )
# y = 3 * x + 2 예측값은 # [[32.023582]] # 에포크 늘림으로써 더 근사한 값을 예측했다.


##################################################################################################################
#     #[2] 모델 컴파일
# model.compile(optimizer = 'sgd', loss = 'mse', metrics = ['mae'])
#     #[3] 모델 훈련
# # model.fit(키,몸무게,epochs = 1200) # x(독립변수) y(종속변수)를 1200번 학습 #loss 오차 #mae
# history = model.fit(x,y,epochs = 20) # x(독립변수) y(종속변수)를 1200번 학습 #loss 오차 #mae 절대오차
# print(history)
#     #[4] 시각화
# plt.plot(history.history['loss'])
# plt.plot(history.history['mae'])
# plt.show()