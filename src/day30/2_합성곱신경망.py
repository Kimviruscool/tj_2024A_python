#2. 합성곱 신경망

import tensorflow as tf
import matplotlib.pyplot as plt

#데이터 셋 10 가지 종류의 이미지 데이터셋[비행기,자동차,새,고양이,사슴,개,개구리,말,배,트럭]
cifar10 = tf.keras.datasets.cifar10

#칼라 이미지의 합성곱 모델 만들기
(x_train,y_train),(x_valid,y_valid) = cifar10.load_data()
print(x_train.shape)
#(50000, 32, 32, 3)

#데이터 전처리

#최소값 최댓값 확인
print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#정규화
x_train = x_train / 255.0
x_valid = x_valid / 255.0

print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#채널 추가
print(x_train.shape,x_valid.shape)

x_train_in = x_train [...,tf.newaxis]
x_valid_in = x_valid [...,tf.newaxis]

print(x_train_in.shape, x_valid_in.shape)

#모델 생성
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3),name='conv'),
    tf.keras.layers.MaxPooling2D((2,2),name='pool'),

    #################최적 파라미터 찾기 2.
    # 레이어 추가
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),  # 32개 노드를 가지는 완결 레이어 1개추가

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=15)

############################################ 예측
#1. 파이썬 OpenCV : 이미지파일을 파이썬으로 호출 하는 모듈 제공
import cv2

#2. 외부 이미지 가져오기
img = cv2.imread('cat.png')
print(img)

#3. 이미지 사이즈 변경
img = cv2.resize(img, dsize=(32,32) ) #모델의 사이즈와 동일하게 변경
print(img.shape)
#정규화
img = img / 255.0

#4. 변경된 이미지 시각화
# cv2.imshow('img', img)
# cv2.waitKey()

#5. 모델을 이용한 새로운 이미지 예측하기
result = model.predict(img[tf.newaxis,...]) #(32,32,3) > (1,32,32,3)
print(tf.argmax(result[0]).numpy()) #가장 높은 확률을 가진 종속변수

# 데이터셋[비행기,자동차,새,고양이,사슴,개,개구리,말,배,트럭]
        #   0    1   2    3    4  5    6  7   8  9

#1. 정규화 안했더니 예측값 8 # 정규화 이후 8
# 레이어추가 , 에포크 설정으로 5

#자동차
#결과값 : 9

#고양이
#결과값 : 1