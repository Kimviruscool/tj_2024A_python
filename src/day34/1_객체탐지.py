#1_객체탐지.py

import tensorflow as tf

img_path = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Gangnam_Seoul_January_2009.jpg/1280px-Gangnam_Seoul_January_2009.jpg'
img = tf.keras.utils.get_file(fname='gangnam', origin=img_path) #지정한 경로의 이미지를 파일로 가져오기
print(img)
#파일 객체를 String 변환
img = tf.io.read_file(img)
print(img)
# 문자를 숫자(텐서)변환
img = tf.image.decode_jpeg(img, channels=3)
print(img)
# 0~1 범위로 정규화
img = tf.image.convert_image_dtype(img, tf.float32)
print(img)
# 시각화
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

#차원
print(img.shape) #(700, 1280, 3)
img_input = tf.expand_dims(img,0) #0번 인덱스 (가장 앞)(앞에) 차원 추가
print(img_input.shape) #(1, 700, 1280, 3)

#외부로부터 사전 학습 된 모델 가져오기
import tensorflow_hub as tfhub
#지정한 URL이용한 모델 로드 하기
model = tfhub.load('https://www.kaggle.com/models/google/faster-rcnn-inception-resnet-v2/tensorFlow1/faster-rcnn-openimages-v4-inception-resnet-v2/1?tfhub-redirect=true')
 #모델 시그니처(용도) 확인
print(model.signatures.keys())
obj_detector = model.signatures['default']
print(obj_detector)

#로드한 모델로 예측하기
result = obj_detector(img_input)
print(result.keys()) #경계박스 좌표 , 예측한/검출된 클래스(정답) 아이디, 예측/검출된 확률/스코어
print(len(result['detection_scores']))

#예측한 결과 시각화
boxes = result["detection_boxes"]
labels = result["detection_class_entities"]
scores = result["detection_scores"]

#샘플 이미지 가로 세로 크기
img_height,img_width=img.shape[0],img.shape[1]

#탐지할 최대 객체의 수
obj_to_detect = 10

# 시각화
plt.figure(figsize=(15,10))
for i in range(min(obj_to_detect,boxes.shape[0])):
    if scores[i] >= 0.2:
        (ymax,xmin,ymin,xmax) = (boxes[i][0]*img_height,boxes[i][1]*img_width,
                                 boxes[i][2]*img_height,boxes[i][3]*img_width)

        plt.imshow(img)
        plt.plot([xmin, xmax, xmax, xmin, xmin],[ymin,ymin,ymax,ymax,ymin],color="yellow",linewidth=2)

        class_name = labels[i].numpy().decode('utf-8')
        infer_score = int(scores[i].numpy()*100)
        annotation = "{}:{}%".format(class_name,infer_score)
        plt.text(xmin+10,ymax+20,annotation,color="white",backgroundcolor='blue',fontsize=10)

plt.show()