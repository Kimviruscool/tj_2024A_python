# 1.위성이미지분류

# (1) 데이터 수집
# (2) 데이터 전처리 / 데이터 분할
# (3) 모델 설계
# (4) 모델 컴파일
# (5) 모델 학습 > 모델 튜닝(최적의 하이퍼 파라미터 값 찾기) > (3)
# (6) 모델 평가 및 예측

import tensorflow as tf
import numpy as np
import json
import matplotlib.pylab as plt

# Tensorflow dataset 활용
import tensorflow_datasets as tfds
from jinja2.optimizer import optimize
from joblib.numpy_pickle_utils import BUFFER_SIZE
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics
from tensorflow.python.ops.linalg.linalg_impl import transpose
from tensorflow_datasets.image_classification.corruptions import brightness

# EuroSAT 위성 사진 데이터셋 로드
DATA_DTR = "dataset/"

(train_ds, valid_ds), info = tfds.load("eurosat/rgb", split=['train[:80%]', 'train[80%:]'],  # 80데이터 훈련용 20검증용 분할
                                       shuffle_files=True,  # 파일을 무작위로 섞어 데이터를 로드한다.
                                       as_supervised=True,  # 이미지와 레이블로 구성된 튜플로 가져오기
                                       with_info=True,  # 데이터셋의 메타(데이터셋설명)정보 가져오기
                                       data_dir=DATA_DTR)  # 현재 py 파일이 위치한 폴더내 하위 폴더로 'dataset' 폴더안에 '데이터셋' 을 다운로드 하겠다.
print(train_ds)
print(valid_ds)
print(info)

# 데이터 확인
tfds.show_examples(train_ds, info)

# as_dataframe 사용하여 샘플 출력
tfds.as_dataframe(valid_ds.take(10), info)

# 목표 클래스의 개수
NUM_CLASSES = info.features["label"].num_classes
print(NUM_CLASSES)

# 숫자 레이블을 활용해 문자열 메타 데이터로 변환
print(info.features['label'].int2str(6))  # PermanentCrop : 영구작물
# 0경작지,1숲,2식물,3고속도로,4산업지역,5목초지,6영구작물,7주거지역,8강,9바다/호수

### 데이터 전처리

# 데이터 전처리 파이프 라인
BATCH_SIZE = 64  # 배치란? 한버넹 처리하는  데이터의 묶음 단위 의미한다.
# 데이터를 배치로 나눠서 처리하면 메모리 사용을 최적할수있다.
# 모델이 전체를 한번에 처리하지 않고 데이터를 묶음(배치) 단위로 나누어 처리한다.
BUFFER_SIZE = 1000  # 버퍼란 ? 임시 저장공간


# 셔플 할때 버퍼에 1000을 가져와서 임시로 저장하는 공간
# 셔플 : 일반적으로 정형화된 데이터들을 순서대로 넣으면 모델의 특정 패턴이 치우치게 될수 있기 때문에 섞어준다.


def preprocess_data(image, label):
    image = tf.cast(image, tf.float32) / 255.0  # 이미지타입을 float32 변환하고 #0~255 > 0,1 정규화
    return image, label  # 이미지와 레이블을 튜플구조로 변환하기 #() 생략 가능


# num_parallel_calls=tf.data.AUTOTUNE : 병렬처리(병렬 매핑)
train_data = train_ds.map(preprocess_data, num_parallel_calls=tf.data.AUTOTUNE)
valid_data = valid_ds.map(preprocess_data, num_parallel_calls=tf.data.AUTOTUNE)

# 훈련용 데이터를 셔플링(가중치-업데이트O) 하고 캐시(기록) 제외한 오토튠을 적용했다 .
# 검증용 데이터는 셔플링(가중치-업데이트X) 하지 않고 캐시(기록) 하고 오토튠을 적용했다.
train_data = train_data.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
valid_data = valid_data.batch(BATCH_SIZE).cache().prefetch(tf.data.AUTOTUNE)


# cache() : 캐시(기록)란 검증데이터셋 메모리를 캐시한다.
# 한번 호출한 검증데이터는 메모리에 기록하여 다음에 호출 시 빠르게 접근할 수 있도록 하는 함수

### 모델 훈련 및 검증

# Sequential API를 사용하여 샘플 모델 생성

def build_model():
    model = tf.keras.Sequential([

        # Convolution 층 (레이어 (은닉층) )
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        # Classfier 출력층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
    ])

    return model


model = build_model()

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 훈련
history = model.fit(train_data, validation_data=valid_data, epochs=5)
import matplotlib.pyplot as plt

def plot_loss_acc(history, epoch):
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    #
    fig , axes =plt.subplots(1,2)

    axes[0].plot(range(1,epoch+1),loss)
    axes[0].plot(range(1,epoch+1),val_loss)
    axes[0].set_title('loss')

    axes[1].plot(range(1,epoch+1),acc)
    axes[1].plot(range(1,epoch+1),val_acc)
    axes[1].set_title('accuracy')

    plt.show()

# 손실함수 정확도 그래프 그리기
plot_loss_acc(history,3)

### 데이터 증강
image_batch, label_batch = next(iter(train_data.take(1)))

image = image_batch[0]
label = label_batch[0].numpy()

plt.imshow(image)
plt.title(info.features["label"].int2str(label))


# 데이터 증강 전후를 비교하는 시각화 함수를 정의
def plot_augmentation(original, augmented):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].imshow(original)
    axes[0].set_title('Original')

    axes[1].imshow(augmented)
    axes[1].set_title("Augmented")

    plt.show()


# 좌우 뒤집기
lr_flip = tf.image.flip_left_right(image)
plot_augmentation(image, lr_flip)

# 상하 뒤집기
up_flip = tf.image.flip_up_down(image)
plot_augmentation(image, up_flip)

# 회전
rotate90 = tf.image.rot90(image)
plot_augmentation(image, rotate90)

# transpose
transpose = tf.image.transpose(image)
plot_augmentation(image, transpose)

# 이미지 자르기1
crop1 = tf.image.central_crop(image, central_fraction=0.6)
plot_augmentation(image, crop1)

# 이미지 자르기2
img = tf.image.resize_with_crop_or_pad(image, 64 + 20, 64 + 20)  # 사이즈 키우기
crop2 = tf.image.random_crop(img, size=[64, 64, 3])
plot_augmentation(image, crop2)

# 이미지 밝기
brightness = tf.image.adjust_brightness(image, delta=0.3)
plot_augmentation(image, brightness)

# 이미지 채도
saturation = tf.image.adjust_saturation(image, saturation_factor=0.5)
plot_augmentation(image, saturation)

# 이미지 대비
contrast = tf.image.adjust_contrast(image, contrast_factor=2)
plot_augmentation(image, contrast)


# 이미지 증강 전처리
def data_augmentation(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_flip_up_down(image)
    image = tf.image.random_brightness(image, max_delta=0.3)
    image = tf.image.random_crop(image, size=[64, 64, 3])

    image = tf.cast(image, tf.float32) / 255.0

    return image, label


train_aug = train_ds.map(data_augmentation, num_parallel_calls=tf.data.AUTOTUNE)
valid_aug = valid_ds.map(data_augmentation, num_parallel_calls=tf.data.AUTOTUNE)

train_aug = train_aug.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
valid_aug = valid_aug.batch(BATCH_SIZE).cache().prefetch(tf.data.AUTOTUNE)

print(train_aug)
print(valid_aug)

# 모델 생성
aug_model = build_model()

# 모델 컴파일
aug_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
aug_history = aug_model.fit(train_aug, validation_data=valid_aug, epochs=5)

# 손실함수 정확도 그래프 그리기
# plot_loss_acc(aug_history,50)

### ResNet 사전 학습 모델
from tensorflow.keras.applications import ResNet50V2

pre_trained_base = ResNet50V2(include_top=False, weights='imagenet', input_shape=[64, 64, 3])

# 사전 학습된 가중치를 업데이트 되지 않도록 설정
pre_trained_base.trainable = False


# 모델구조시각화

# Top층에 Classifier 추가
def build_trainsfer_classifier():
    model = tf.keras.Sequential([
        pre_trained_base,
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
    ])

    return model


# 모델구조
tc_model = build_trainsfer_classifier()
tc_model.summary()

# 모델 컴파일
tc_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
tc_history = tc_model.fit(train_aug, validation_data=valid_aug, epochs=5)

# 손실함수 정확도 그래프 그리기
# plot_loss_acc(tc_history, 50)
