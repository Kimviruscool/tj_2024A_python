import numpy as np
import pandas as pd

data_df = pd.read_csv("auto_mpg.csv", header=0, engine="python")
# print(data_df.shape) (398, 9)
# print(data_df.head())

data_df = data_df.drop(['car_name','origin','horsepower'],axis=1, inplace=False)
# print(data_df.head())
# print(data_df.shape) #(398, 6)
# print(data_df.info())

from sklearn.linear_model import LinearRegression #모델 객체 생성
from sklearn.model_selection import train_test_split #모델 train test 나누기
from sklearn.metrics import mean_squared_error,r2_score #MSE,R² 값 분석

#X,Y 분할하기
Y = data_df['mpg'] #타겟
X = data_df.drop(['mpg'], axis = 1, inplace=False) #피처

#훈련용 평가용 분할
x_train, x_test , y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state= 0) #비율 7:3 #난수시드 0

#선형회귀분석 모델 생성
lr = LinearRegression()
#모델에 피팅
lr.fit(x_train,y_train)
#선형 회귀 분석 예측 값 생성 
y_predict = lr.predict(x_test)

MSE = mean_squared_error(y_test, y_predict)
print(MSE) #평균 제곱오차 #12.278239036609486
RMSE = np.sqrt(MSE)
print(RMSE) #루트 평균 제곱 오차 #3.5040318258556793
r2 = r2_score(y_test, y_predict)
print(r2) #결정계수 #0.8078579451877166

print("Y 절편 값 : ", np.round(lr.intercept_, 2)) #Y 절편 값 :  -17.55
print("회귀 계수 값 :", np.round(lr.coef_, 2)) #회귀 계수 값 : [-0.14  0.01 -0.01  0.2   0.76]

coef = pd.Series(data = np.round(lr.coef_,2), index=X.columns) #Seriees 자료형만들기
coef.sort_values(ascending = False) #내림차순정렬
# print(coef)

################ 시각화 ##################
import matplotlib.pyplot as plt
import seaborn as sns
fig,axs = plt.subplots(figsize=(16,16), ncols=3, nrows=2)
x_feature = ['model_year','acceleration','displacement','weight','cylinders']
plot_color = ['r','b','y','g','r']
for i, feature in enumerate(x_feature) :
    row = int(i/3)
    col = i%3
    sns.regplot(x = feature , y = 'mpg', data = data_df, ax = axs[row][col], color=plot_color[i])
plt.show()

###################### 예측 #######################
print("연비를 예측하고 싶은 차의 정보를 입력해주세요.")

cylinders_1 = int(input("cylinders : "))
displacement_1 = int(input("displacement : "))
weight_1 = int(input("weight : "))
acceleration_1 = int(input("acceleration : "))
model_year_1 = int(input("model_year : "))

mpg_predict = lr.predict([[cylinders_1,displacement_1,weight_1,acceleration_1,model_year_1]])

print(f"이 자동차의 예상 연비는(MPG)는 {mpg_predict} 입니다.")