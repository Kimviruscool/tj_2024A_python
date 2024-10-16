import zipfile

import tf
from numpy.lib.function_base import extract

#데이터준비 교재와다르게 로컬 PC에서 준비
import zipfile
import os
import tensorflow as tf

source_filename = 'cat-and-dog.zip'
extract_folder = 'c:/dataset'
with zipfile.ZipFile(source_filename,'r') as zipObj :
    zipObj.extractall(extract_folder)
# zipfile.ZipFile(source_filename,'r') as zipObj : zip파일 을 읽기모드를 읽어와서 zipObj 변수에 담기
    #파일객체변수명.extractall(압축해제할폴더경로)
#훈련용 검증 용 저장위치 지정 : C:\dataset\archive
train_dir = os.path.join(extract_folder, "archive/training_set/training_set")
valid_dir = os.path.join(extract_folder, "archive/test_set/test_set")
print(train_dir)
print(valid_dir)

#2. 정규화
from tensorflow.keras.preprocessing.image import ImageDataGenerator #모듈 호출
image_gen = ImageDataGenerator(rescale=1/255.0) #RGB 이미지 0~255 에서 > 0~1 로 구성

#3. 한번에 많은 데이터를 처리 > 이미지 제너레이터
train_gen = image_gen.flow_from_directory(train_dir, #훈련용 데이터 저장된 위치
                                          batch_size=32, #배치 단위
                                          target_size=(224,224),
                                          classes = ['cats','dogs'],
                                          class_mode='binary',
                                          seed = 2020
                                          )

valid_gen = image_gen.flow_from_directory(valid_dir, #훈련용 데이터 저장된 위치
                                          batch_size=32, #배치 단위
                                          target_size=(224,224),
                                          classes = ['cats','dogs'],
                                          class_mode='binary',
                                          seed = 2020
                                          )

class_labels = ['cats','dogs']
batch = next(train_gen)
images = batch[0]
labels = batch[1]

import matplotlib.pyplot as plt
for i in range(32) :
    ax = plt.subplot(4,8,i+1)
    plt.imshow(images[i])
    plt.title(class_labels[ int(labels[i]) ])
    plt.axis("off")
plt.show()

def build_model():
    model = tf.keras.Sequential([

        #Convolution 층
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32,(3,3),padding='same',activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),

        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64,(3,3),padding='same',activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),

        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(128,(3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256,activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1,activation='sigmoid')
    ])
    return model

model = build_model()

model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_gen,validation_data=valid_gen, epochs=10)

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

plot_loss_acc(history, 10)