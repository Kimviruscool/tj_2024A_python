#1_합성곱신경망

'''
- 딥러닝 프로세스(절차)
1. 데이터 수집
2. 데이터 전처리 : 수집된 데이ㅓ터를 신경망 모델에 적합하게 
3. 데이터 분할 : 훈련용데이터 와 검증/데이터 용 으로 나눈다. 주로 7:3 VS 8:2
4. 모델 설계(구축)
    1. Sequential API, Functional API
    2. 레이어 구성(많을 수록 손실률 감소) : 입력층 > 은닉층1,2,3(Conv2D,Flatten,Maxpooling2D)등등 > 출력층 구성
    3. 활성화 함수 : 각 레이어 에서 학습된 값을 비선형으로 변환할때 사용, 주로 Relu, sofrmax 함수 사용
    4. 손실 함수

5. 모델 컴파일 : 모델을 어떻게 학습 하고 평가 하는지 설정
    1. 옵티마이저 : 모델의 가중치를 업데이트 하는 방법의 알고리즘/계산법, adam : 학습률 기반으로 최적화 알고리즘 , sgd : 확률적 경사 하강법
    2. 손실함수 : 실제값 과 예측값과의 차이 , 분류모델 : sparse_categorical_crossentropy, 회귀 : mean_squared_error
    3. 평가지표 : 모델의 성능을 평가하는 지표, 분류모델 : accuracy, 회귀 : mse
6. 모델 학습
    1. 에포크 : 전체 훈련 데이터를 한 번 사용되는 것을 1에포크 , 10에포크 이면 전체 훈련을 10번
    2. 검증 : validation_data 학습 중에 검증/테스트 데이터를 사용하여 모델의ㅐ 손실 평가를 확인할수 있다.
7. 모델 평가 > 모델 튜닝(하이퍼 파라미터(변수))
    1. evaluation() : 최종 성능의 손실함수 와 평가지표 결과를 볼수 있다.
# >>>>>>> 모델 튜닝 (하이퍼 파라미터)
    학습률 , 배치크기 , 레이어수 , 노드(뉴런) 수 , 활성화 함수 , 에포크 등등 여러 하이퍼파라미터 조정하기.
8. 모델 예측
    1. predict()
'''

import tensorflow as tf
import numpy as np
from jinja2.optimizer import optimize
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_valid,y_valid) = mnist.load_data()

print(x_train.shape,y_train.shape)
print(x_valid.shape,y_valid.shape)

#새로운 출력 값 배열 생성(홀수 : 1 짝수 : 0 )
y_train_odd = []
for y in y_train :
    if y%2==0:
        y_train_odd.append(0)
    else:
        y_train_odd.append(1)

y_train_odd = np.array(y_train_odd)
print(y_train_odd.shape)

print(y_valid[:10])
print(y_train_odd[:10])

#validation 데이터셋 처리
y_valid_odd = []
for y in y_valid:
    if y % 2 == 0 :
        y_valid_odd.append(0)
    else :
        y_valid_odd.append(1)

y_valid_odd = np.array(y_valid_odd)
print(y_valid_odd.shape)

#정규화
x_train = x_train / 255.0
x_valid = x_valid / 255.0

#채널 추가
x_train_in = tf.expand_dims(x_train , -1)
x_valid_in = tf.expand_dims(x_valid , -1)

print(x_train_in.shape,x_valid_in.shape)

#Functional API를 사용하여 모델 생성

############### 합성곱 입력구조 ###########################
#입력레이어
inputs = tf.keras.layers.Input(shape=(28,28,1))

# 방법 1 -
#합성곱 레이어
conv = tf.keras.layers.Conv2D(32,(3,3),activation='relu')(inputs)
# 방법 2 -
#합성곱 레이어 앞에 입력레이어 연결하기 #__call__ #입력레이어 < 합성곱레이어
#conv = tf.keras.layers.Conv2D(32,(3,3),activation='relu')
#conv(inputs)

#풀링 레이어
pool = tf.keras.layers.MaxPooling2D((2,2))(conv)

#플레톤 레이어
flat = tf.keras.layers.Flatten()(pool)

############### 단순 입력구조 추가 ###########################
flat_inputs = tf.keras.layers.Flatten()(inputs)

############### 2개 입력 구조를 1개 출력으로 만들기 #합치기 ############################
#출력레이어
concat = tf.keras.layers.Concatenate()([flat,flat_inputs])
outputs = tf.keras.layers.Dense(10,activation='softmax')(concat)

#모델
model = tf.keras.models.Model(inputs = inputs, outputs = outputs)

print(model.summary())

# #모델 구조 출력 및 이미지 파일로 저장
# from tensorflow.python.keras.utils.vis_utils import plot_model
# plot_model(model, show_shapes=True, show_layer_names=True, to_file='functional_cnn.png')

#모델 컴파일
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)

#모델 성능
val_loss , val_acc = model.evaluate(x_valid_in,y_valid)
#정확도 98% 손실률 0.6%

print(val_loss,val_acc)
#0.05295292288064957 0.9846000075340271

#다중 출력 분류 모델

# Functional API를 사용해 모델 생성
inputs = tf.keras.layers.Input(shape=(28,28,1), name='inputs')

conv=tf.keras.layers.Conv2D(32,(3,3),activation='relu',name='conv2d_layer')(inputs)
pool = tf.keras.layers.MaxPooling2D((2,2),name='maxpool_layer')(conv)
flat = tf.keras.layers.Flatten(name='flatten_layer')(pool)

flat_inputs = tf.keras.layers.Flatten()(inputs)
concat = tf.keras.layers.Concatenate()([flat,flat_inputs])
digit_outputs = tf.keras.layers.Dense(10,activation='softmax',name='digit_dense')(concat)

odd_outputs = tf.keras.layers.Dense(1,activation='sigmoid',name='odd_dense')(flat_inputs)

model = tf.keras.models.Model(inputs=inputs,outputs=[digit_outputs,odd_outputs])
print(model.summary())

#모델의 입력과 출력을 나타내는 텐서
print(model.input)
print(model.output)

#모델 컴파일
model.compile(optimizer='adam',
              loss={'digit_dense':'sparse_categorical_crossentropy','odd_dense':'binary_crossentropy'},
              loss_weights={'digit_dense':1,'odd_dense':0.5}, #손실함수 가중치 # 1: 100% , 0.5 : 50%
              #0~9 예측 결과는 100% 반영하고 활짝예측/결과 는 50%반영 설정 #모델 손실계산에 사용할 비중(가중치)
              metrics={'digit_dense' : ['accuracy'],'odd_dense' : ['accuracy']})
#모델 훈련
history = model.fit({'inputs':x_train_in},
                    {'digit_dense':y_train,'odd_dense':y_train_odd},
                    validation_data=({'inputs':x_valid_in},{'digit_dense':y_valid,'odd_dense':y_valid_odd}),
                    epochs=10)

#모델 성능 평가
model.evaluate({'inputs':x_valid_in},{'digit_dense':y_valid,'odd_dense':y_valid_odd})

import matplotlib.pyplot as plt

def plot_image(data, idx):
    plt.figure(figsize=(5,5))
    plt.imshow(data[idx])
    plt.axis("off")
    plt.show()

plot_image(x_valid,0)

#모델 예측
print(y_valid[0]) #정답 7
digit_preds, odd_preds = model.predict(x_valid_in) #예측
print(digit_preds[0])
print(odd_preds[0])

digit_labels = np.argmax(digit_preds, axis=-1)
print(digit_labels[0:10])

odd_labels = (odd_preds > 0.5).astype(np.int32).reshape(1,-1)[0]
print(odd_labels[0:10])

#전이학습 Tensorflow Learning
#앞에 모델에서 flatten_layer 출력을 추출
base_model_output = model.get_layer('flatten_layer').output

#앞의 출력을 출력으로 하는 모델 정의
base_model = tf.keras.models.Model(inputs=model.input, outputs=base_model_output, name='base')
print(base_model.summary())

#Sequential API적용
digit_model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.Dense(10,activation='softmax')
])

print(digit_model.summary())

#모델 컴파일
digit_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history = digit_model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)

#베이스 모델의 가중치 고정(Freeze Model)
base_model_frozen = tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen')
base_model_frozen.trainable = False
print(base_model_frozen.summary())

#Functional API적용
dense_output = tf.keras.layers.Dense(10,activation='softmax')(base_model_frozen.output)
digit_model_frozen = tf.keras.models.Model(inputs=base_model_frozen.input,outputs=dense_output)
print(digit_model_frozen.summary())

#모델 컴파일
digit_model_frozen.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history = digit_model_frozen.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)

#베이스 모델의 Conv2D 레이어의 가중치만 고정(Freeze Layer)
base_model_frozen2= tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen2')
base_model_frozen2.get_layer('conv2d_layer').trainable = False
print(base_model_frozen2.summary())

#Functional API적용
dense_output2 = tf.keras.layers.Dense(10,activation='softmax')(base_model_frozen2.output)
digit_model_frozen2 = tf.keras.models.Model(inputs=base_model_frozen2.input,outputs=dense_output2)
print(digit_model_frozen2.summary())

#모델 컴파일
digit_model_frozen2.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#모델 훈련
history = digit_model_frozen2.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)