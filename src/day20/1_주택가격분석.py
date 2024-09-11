#day20 > 1_주택가격분석.py
# //////// 데이터 수집및 분석 //////////////////////
import pandas as pd
# from sklearn.datasets import load_boston
# boston = load_boston()
# print(boston)

# import pandas as pd
import numpy as np
from pyexpat import features

data_url = "http://lib.stat.cmu.edu/datasets/boston" #보스턴 주택 정보가 있는 url
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None) #url
#지정한 url에서 데이터프레임으로 가져오기
# sep = "\s+" : 데이터 간의 공백으로 구분된 csv
#skiprow = 22 : 위에서부터 22행 까지 생략
#header=None: 헤더가 없다는 뜻
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
print(data.shape) #주택관련변수들 : 독립변수 , 피처(feature) , 메소드
print(target.shape) #(주택가격) : 종속변수 , 타겟, 타겟변수
#독립변수의 이름
feature_names = ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
#데이터 프레임 생성
boston_df = pd.DataFrame(data, columns=feature_names)
# print(boston_df.head())
#데이터프레임의 주택가격 열 추가
boston_df['PRICE'] = target
# print(boston_df.head())
# print(boston_df.shape) #506, 14 행개수, 열개수
# print(boston_df.info()) #열이름, 열데이터수 , 데이터타입, 메모리
########################## [2] 분석 모델 구축, 결과 분석 #################
#1. 타겟 과 피처 분할 하기
Y = boston_df['PRICE'] #종속변수 , 타겟 #주택가격
X = boston_df.drop(['PRICE'], axis=1, inplace=False ) #독립변수 , 피처 #주택가격 외 정보
#2. 훈련용 과 평가용 분할 하기
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.3, random_state=156)
#1.훈련용독립변수 테스트독립변수 훈련용종속변수 테스트종속변수 train_test_split(독립변수, 종속변수, test_size = 분할비율 , random_state=난수생성시드 )
#test_size = 0.3  : 훈련용 70% ,테스트용 30% 분할
print(xtrain.shape) #(354, 13)
print(xtest.shape) #(152, 13)
#3. 선형 회귀 분석 모델 생성
from sklearn.linear_model import LinearRegression #모델 구축
model = LinearRegression() #훈련 모델 객체 생성
model.fit(xtrain, ytrain) #훈련 데이터를 사용한 모델 피팅 

#4. 모델 훈련
print(model.intercept_) #40.995595172164506 #Y절편

print(model.coef_) #회귀계수
# #[-1.12979614e-01  6.55124002e-02  3.44366694e-02  3.04589777e+00
#  -1.97958320e+01  3.35496880e+00  5.93713290e-03 -1.74185354e+00
#   3.55884364e-01 -1.42954516e-02 -9.20180066e-01  1.03966156e-02
#  -5.66182106e-01]

#5. 테스트용으로 예측하기
    #테스트용에 있는 주택 정보를 이용한 주택 가격 예측하기
y_pred = model.predict(xtest) 
print(y_pred)
#152개의 가격 예측

#6. 평가지표 확인하기 (MSE,RMSE,결정계수,y절편,회귀계수)
#ytest # 동일한 피처(독립변수) 정보를 가진 실제 주택가격
#y_pred # 동일한 피처(독립변수) 정보를 가진 예측한 주택가격

from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error(ytest, y_pred) #평균의 절대오차
print(MAE) #3.2136683441244496

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(ytest, y_pred) #평균제곱 오차
print(MSE) #17.296915907902093

RMSE = np.sqrt(MSE) #루트 평균 제곱 오차
print(RMSE) #4.158956107955708

from sklearn.metrics import r2_score
r2 = r2_score(ytest, y_pred) #R² (결정계수)
print(r2) #0.757226332313893
print(np.round(model.coef_, 1))
#[ -0.1   0.1   0.    3.  -19.8   3.4   0.   -1.7   0.4  -0.   -0.9   0.
# -0.6]
###################### [3] 결과 시각화 ###############################
import matplotlib.pyplot as plt
import seaborn as sns #회귀 분석 관련 차트 구성

# sns.regplot(x='CRIM', y='PRICE', data=boston_df)
# - y절편 : 독립변수가 0일때 종속변수의  값
# - 회귀계수 : 독립변수 1증가 할때마다 종속변수의 증감 단위 #기울기
# - 신뢰구간 : 좁으면 예측이 안정적이고 관계가 명확하다.
#             넓다면 예측이 불안정하고 관계가 불명확 하다.
fig, axs = plt.subplots(figsize = (16,16), ncols=3, nrows=5) #3칸 5줄로 구성된 다중차트

x_feature= ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

for i, feature in enumerate(x_feature) : # for 인덱스 , 요소값 in enumerate(리스트)
    print(i)
    print(feature)
    row = int(i/3) #몫
    col = i%3 #나머지
    sns.regplot(x = feature, y='PRICE', data=boston_df, ax=axs[row][col])
plt.show()