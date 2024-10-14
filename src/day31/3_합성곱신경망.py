#3_합성곱 신경망

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from jinja2.optimizer import optimize
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics

#1. 데이터셋 로드, 10가지 종류의 의류 이미지 데이터셋
# Lable Description
# 0. T-shirt : 티셔츠
# 1. Trouser : 바지
# 2. Pullover : 스웨터
# 3. Dress : 드레스
# 4. Coat : 코트
# 5. Sandal : 샌들
# 6. Shirt : 셔츠
# 7. Sneaker : 신발
# 8. Bag : 가방
# 9. Ankle boot : 부츠
#mnist 데이터이미지 호출
fashion_mnist = tf.keras.datasets.fashion_mnist
# 실제 , 훈련용 데이터 셋 = 데이터 호출 적용
(x_train,y_train),(x_valid,y_valid) = fashion_mnist.load_data()
print(x_train.shape)

#Functional Api 이용한 모델 생성(다중 입력) 과 예측 테스트

#정규화
x_train = x_train / 255.0
x_valid = x_valid / 255.0

print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#채널추가
x_train_in = x_train [...,tf.newaxis]
x_valid_in = x_valid [...,tf.newaxis]

print(x_train_in.shape,x_valid_in.shape)

#### 모델 생성
# 입력층
inputs = tf.keras.layers.Input(shape=(28,28,1))
# 은닉(합성곱 레이어)
conv = tf.keras.layers.Conv2D(32,(3,3),activation='relu')(inputs)
# 은닉(풀링 레이어)
pool = tf.keras.layers.MaxPooling2D((2,2))(conv)
# 은닉(플레톤 레이어)
flat = tf.keras.layers.Flatten()(pool)

##### 단순 입력구조 추가
flat_inputs = tf.keras.layers.Flatten()(inputs)
# 연결
concat = tf.keras.layers.Concatenate()([flat,flat_inputs])
# 출력층
outputs = tf.keras.layers.Dense(10,activation='softmax')(concat)

#모델
model = tf.keras.models.Model(inputs=inputs , outputs = outputs)

model.summary()

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)
########################################################################
import cv2

img = cv2.imread('tee.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)

img = cv2.resize(img, dsize=(28,28))
print(img.shape)

#정규화
img = img/255.0

result = model.predict(img[tf.newaxis,...])
print(tf.argmax(result[0]).numpy())

# 가방이미지 예측
#나올값: 8
#나온값: 8

#티 예측
#나올값: 0
#나온값: 8