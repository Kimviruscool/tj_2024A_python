import tensorflow as tf
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics

#1. 데이터셋
fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train,y_train),(x_valid,y_valid) = fashion_mnist.load_data()
print(x_train.shape)

#데이터 시각화
import matplotlib.pyplot as plt
plt.imshow(x_train[0])
# plt.show()

#위 데이터셋을 이용한 합성곱 모델 구축하고 학습하여 정확도 (accuracy) 95%이상 되도록 파라미터 설정하시오.


# 데이터 전처리

#최솟값 최댓값확인
print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#정규화
x_train = x_train / 255.0
x_valid = x_valid / 255.0

print(x_train.min(),x_train.max()) #0~1
print(x_valid.min(),x_valid.max()) #0~1

#채널추가
print(x_train.shape,x_valid.shape)

x_train_in = x_train [..., tf.newaxis]
x_valid_in = x_valid [..., tf.newaxis]

print(x_train_in.shape,x_valid_in.shape)

#모델생성
model = tf.keras.Sequential([
    #합성곱 레이어 :
    #   Conv2D( 특성맵수,( 필터(커널영역단위) )),activation='활성화함수', input_shape=(가로픽셀,세로픽셀,채널(흑백1칼라3))
    tf.keras.layers.Conv2D(32,(3,3), activation='relu', input_shape=(28,28,1),name='conv'),
    #풀링 레이어 : 최댓값 풀링 설정
    tf.keras.layers.MaxPooling2D((2,2),name='pool'),

    #################최적 파라미터 찾기 2.
    # 레이어 추가
    tf.keras.layers.Dense(32, activation='relu'), #32개 노드를 가지는 완결 레이어 1개추가


    # 플래톤 레이어 : 학습된결과 의 다차원을 1차원 배열로 변환
    tf.keras.layers.Flatten(),
    # 출력 레이어 : 종속변수의 결과 종류가 10개라서 10, 다중분류 : softmax 활성화 함수사용
    tf.keras.layers.Dense(10,activation='softmax')
])

#모델 컴파일
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# model.compile(optimizer(옵티마이저)='adam',
#               loss(손실률)='sparse_categorical_crossentropy(오차 계산법 엔트로피)',
#               metrics(평가지표)=['accuracy'])(정확도)


#훈련
history = model.fit(x_train_in, y_train,validation_data=(x_valid_in,y_valid),epochs=17)

#최적 파라미터 찾기 : 
# 1.epochs 조정 
# 2. layers추가
# 3. 다양한 데이터 준비
# 등등
# 최적한 : 정확도 떨어지지않고 손실값이 증가하지 않는 지점 찾기.

#훈련된 손실, 정확도 파악
print(model.evaluate(x_valid_in,y_valid))
