#2_유방암진단분석.py
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

b_cancer = load_breast_cancer() #사이킷런 내장 데이터 호출
print(b_cancer.DESCR) #내장 데이터 설명서 

b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names) #데이터 프레임으로 변환 #독립변수
b_cancer_df['diagnosis']=b_cancer.target #종속변수 #진단결과
print(b_cancer_df.head())
print('유방암 진단 데이터셋 크기 : ' , b_cancer_df.shape)
print(b_cancer_df.info())
    # 전처리 과정을 이용한 특정 값을 표준화 한 후에 머신러닝 알고리즘을 이용하면 성능을 향상 시킬 수 있다.
from sklearn.preprocessing import StandardScaler #스케일러 : 표준화 전처리

scaler = StandardScaler()
b_cancer_scaler = scaler.fit_transform(b_cancer.data)
print(b_cancer.data[0])
print(b_cancer_scaler[0])

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#X,Y 설정
Y = b_cancer_df['diagnosis']
X = b_cancer_scaler

#훈련용 데이터와 평가용 데이터 분할

X_train , X_test , Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=0) #비율 학습/70:30/평가 #난수시드 0

#로지스틱 회귀분석 : (1) 모델 생성
lr_b_cancer = LogisticRegression()
#로지스틱 회귀분석 : (2) 모델 훈련
lr_b_cancer.fit(X_train, Y_train)
#로지스틱 회귀분석 : (3) 평가 데이터에 대한 예측 수행 > 예측 결과 Y_Predict 구하기
Y_predict = lr_b_cancer.predict(X_test) #이진 예측
Y_predict2 = lr_b_cancer.predict_proba(X_test) #이진 확률 예측
# print(Y_predict)
# print(Y_predict2)

