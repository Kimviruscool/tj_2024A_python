#1_분류분석.py
'''
성형 회귀 모델 : 독립변수(연속형) 종속변수(연속형)
로지스틱 회귀 모델 : 독립변수(연속형) 종속변수(범주형)
이진 분류 문제에서 주로 사용되는 통계 방법
주어진 데이터 기반으로 두 가지 범주 중 하나를 예측하는 모델
    예] 환자가 질병에 걸릴지 여부(1:걸림, 0:안걸림) , 에미일이 스팸 여부(1:스팸,0:정상)
이진 분류 : 두 가지의 결과를 예측
시그모이드 함수 : 두 가지의 결과를 예측 을 확률 값으로 표현 #시그모이드 함수 방정식
'''
import pandas as pd
#1. 예제1 : 공부시간에 따른 합격 여부 예측 모델 구축
#[1] 샘플 데이터
data = {
    "공부시간" : [2,5,1,10,8,12,7,3],
    "합격여부" : [0,1,0,1,1,1,1,0] #1합격 0불합격
}

df = pd.DataFrame(data)
# print(df)

#[2] 독립변수 , 종속변수 분리
x = df[["공부시간"]]
y = df[["합격여부"]]
# print(x)
# print(y)

#[3] 로지스틱 회귀 모델 생성
from sklearn.linear_model import LogisticRegression # LogisticRegression => 로지스틱 회귀 클래스 가져오기
#모델 객체 생성
model = LogisticRegression()
#모델 훈련(피팅)
model.fit(x,y)

#[4] 새로운 공부시간을 이용한 예측 수행 , predict_proba : 모델에서 각 값이 속할 확률 반환 함수
newX = [[6]] #6시간
result = model.predict_proba(newX)
print(result) #[[0.12627315 0.87372685]]
print(result[0][0]) #0.1262731506830168 #12.6% #공부시간이 6시간 일때 0에 속할 확률이 12.6% (불합격)
print(result[0][1]) #0.8737268493169832 #87.3% #공부시간이 6시간 일때 1에 속할 확률이 87.3% (합격)

#2. 예제2 : 쇼핑몰 고객들의 정보를 이용한 구매 확률 분석
#[1] 샘플 데이터
data = {
    "나이" : [25,45,35,50,23,40,30,60],
    "접속횟수" : [50,100,75,120,35,90,60,105],
    "콜라구매여부" : [0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)
#[2] 독립변수 종속변수 분리
x = df[["나이","접속횟수"]]
y = df["콜라구매여부"]

#[3] 로지스틱 회귀 모델 생성
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x,y)

#[4] 새로운 회원정보를 이용한 콜라 구매 예측 수행
newX = [[30,90]]
result = model.predict_proba(newX)
print(result) #[[0.10656662 0.89343338]]
print(result[0][0]) #0.10656661547845592 #10.6%
print(result[0][1]) #0.8934333845215441 #89.3%