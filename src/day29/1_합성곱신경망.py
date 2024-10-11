
import tensorflow as tf

#minist 손글씨 이미지 데이터 로드
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_valid,y_valid) = mnist.load_data()

print(x_train.shape,y_train.shape)
print(x_valid.shape,y_valid.shape)

#샘플 이미지 출력
import matplotlib.pyplot as plt

def plot_image(data, idx):
    plt.figure(figsize=(5, 5))
    plt.imshow(data[idx], cmap='gray')
    plt.axis("off")
    plt.show()

plot_image(x_train, 0)

print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#정규화
x_train = x_train / 255.0
x_valid = x_valid / 255.0

print(x_train.min(),x_train.max())
print(x_valid.min(),x_valid.max())

#채널 추가
print(x_train.shape,x_valid.shape)

x_train_in = x_train[..., tf.newaxis]
x_valid_in = x_valid[..., tf.newaxis]

print(x_train_in.shape,x_valid_in.shape)

#Sequential API를 사용해 샘플 모델 생성
model = tf.keras.Sequential([
    #Convolution 적용(32filters)
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1), name='conv'),
        #32,(3,3) : 32개의 필터를 가진 3*3 크기의 합성곱 레이어 추가
        #relu : Relu 활성화 함수 사용
        #input_shape = (28,28,1) : 독립변수의 차원 모양 (3차원),(가로,세로,채널)
    
    #Max Pooling 적용
    tf.keras.layers.MaxPooling2D((2,2),name='pool'),
        #2*2 크기의 최대 풀링 레이어 추가, 특성맵 크기를 줄인다.

    #Classifier 출력층
    #플래톤 레이어
    tf.keras.layers.Flatten(), #다차원 배열을 1차원 배열로 변환한다.
    
    #출력 레이어
    tf.keras.layers.Dense(10,activation='softmax')
        #종속변수가 분류할 데이터가 0~9 이므로 10개 #다중분류에서는 주로 softmax 활성화 함수를 사용한다.
])

#모델 컴파일 #옵티마이저 #손실함수(엔트로피) #평가지표
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    #옵티마이저 : adam 옵티마이저 로 설정
    #손실함수 : 분류모델 오차 계산법인 엔트로피 설정
    #평가지표 : 분류모델의 정확도 계산법인 accuracy

#모델 훈련
history = model.fit(x_train_in,y_train, #훈련용 데이터 와 훈련용 정답
                    validation_data=(x_valid_in,y_valid), #테스트용 데이터와 테스트용 정답
                    epochs=10) #전체 데이터셋을 10회 반복하여 훈련한다.

#훈련된 손실, 정확도 확인하기
print(model.evaluate(x_valid_in,y_valid)) #테스트용 독립변수 와 테스트용 종속변수(정답)를 평가하기.
#[0.057368457317352295, 0.9836999773979187]

def plot_loss_acc(history, epoch) :
    loss, val_loss = history.history['loss'], history.history['val_loss']
    acc,val_acc = history.history['accuracy'], history.history['val_accuracy']
    
    #서브플롯 차트 구성
    fig, axes = plt.subplots(1,2,figsize=(12,4))
    
    # x축 훈련 수 # y축 훈련 오차 값
    axes[0].plot(range(1,epoch + 1), loss, label="Training") #x축 훈련수 # y축은 훈련 오차 값
    axes[0].plot(range(1, epoch + 1), val_loss, label="Validation") #x 축훈련수 #y축은 테스트 오차 값
    axes[0].legend(loc="best") #이름설정
    axes[0].set_title('Loss')

    axes[1].plot(range(1,epoch + 1), acc, label="Training") # x축 훈련수 #y축 정확도
    axes[1].plot(range(1, epoch + 1), val_acc, label="Validation") #x축 훈련수 #y축은 테스트 정확도
    axes[1].legend(loc="best")
    axes[1].set_title('Accuracy')

    plt.show()

print(y_valid[0]) #종속변수 #10000개 중에 첫번째 손글씨의 정답
print(tf.argmax(model.predict(x_valid_in)[0] ) ) #독립변수 #테스트용으로 예측하기.
# argmax() : 배열내 가장 큰 값을 가진 요소의 인덱스 반환 #7

plot_loss_acc(history, 10)

#모델 구조
print(model.summary())

# 입력 텐서 형태
print(model.inputs)
#[<KerasTensor shape=(None, 28, 28, 1), dtype=float32, sparse=False, name=keras_tensor>]

# 출력 텐서 형태
print(model.outputs)
#[<KerasTensor shape=(None, 10), dtype=float32, sparse=False, name=keras_tensor_4>]

# 레이어
print(model.layers)
#[<Conv2D name=conv, built=True>, <MaxPooling2D name=pool, built=True>, <Flatten name=flatten, built=True>, <Dense name=dense, built=True>]
#Conv2D : 합성곱

# 첫번째레이어선택
print(model.layers[0])
#<Conv2D name=conv, built=True>

# 첫번째 레이어 입력
print(model.layers[0].input)
#<KerasTensor shape=(None, 28, 28, 1), dtype=float32, sparse=False, name=keras_tensor>

# 첫번째 레이어 출력
print(model.layers[0].output)
#<KerasTensor shape=(None, 26, 26, 32), dtype=float32, sparse=False, name=keras_tensor_1>

# 첫번째 레이어 가중치 
print(model.layers[0].weights)
#[<KerasVariable shape=(3, 3, 1, 32), dtype=float32, path=sequential/conv/kernel>, <KerasVariable shape=(32,), dtype=float32, path=sequential/conv/bias>]

# 첫번째 레이어 커널 가중치
print(model.layers[0].kernel)
#<KerasVariable shape=(3, 3, 1, 32), dtype=float32, path=sequential/conv/kernel>

# 첫번째 레이어 bias 가중치
print(model.layers[0].bias)
#<KerasVariable shape=(32,), dtype=float32, path=sequential/conv/bias>

# 레이어 이름 사용하여 레이어 선택
print(model.get_layer('conv'))
#<Conv2D name=conv, built=True>

#샘플이미지의 레이어별 출력을 리스트에 추가(첫번째 , 두번째 레이어)
activator = tf.keras.Model(inputs=model.inputs,outputs=[layer.output for layer in model.layers[:2]])
activations = activator.predict(x_train_in[0][tf.newaxis,...])
print(len(activations))

conv_activation = activations[0]
print(conv_activation.shape)

fig, axes = plt.subplots(4,8)
fig.set_size_inches(10,5)

for i in range(32) :
    axes[i//8, i%8].matshow(conv_activation[0,:,:,i],cmap='viridis')
    axes[i//8, i%8].set_title('kernel %s'%str(i),fontsize=10)
    plt.setp(axes[i//8,i%8].get_xticklabels(),visible=False)
    plt.setp(axes[i//8,i%8].get_yticklabels(),visible=False)

plt.tight_layout()
plt.show()

#두번째 레이어 출력층
pooling_activation = activations[1]
print(pooling_activation.shape)

#시각화
fig, axes = plt.subplots(4,8)
fig.set_size_inches(10,5)

for i in range(32):
    axes[i//8,i%8].matshow(pooling_activation[0,:,:,i],cmap='viridis')
    axes[i//8,i%8].set_title('kernel %s'%str(i), fontsize=10)
    plt.setp(axes[i//8,i%8].get_xticklabels(),visible=False)
    plt.setp(axes[i//8,i%8].get_yticklabels(),visible=False)

plt.tight_layout()
plt.show()