# 4_인천아파트회귀및상관분석

#[1] 가설 : 아파트 층 과 건축년도 증가하면서 아파트 가격도 비싸다.
#[2] 주제 : 아파트 층(종속변수)과 건축년도(종속변수) 에 따른 거래금액(독립변수) 추이 비교
#[3] 분석방법 : 다중 회귀분석, 상관분석

import pandas as pd
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('아파트(매매)_실거래가_20240904134550.csv', encoding='cp949', skiprows=15, thousands=',')
# thousands=',' : 천단위 쉼표 생략 # 천단위 정수타입으로 가져온다.
# print(data)

#과제 : 해당 csv 파일을 분석하여 제출 (한글 깨짐과 무관)
Rformula = '거래금액 ~ 층 + 건축년도'

model = ols(Rformula, data = data).fit()
print(model.params)
'''
Intercept   -1.825623e+06
층            5.751930e+02
건축년도         9.267088e+02
'''
print(model.summary())

#독립변수 거래금액
#족속변수 층 + 년도

fig = plt.figure(figsize = (8,13))
sm.graphics.plot_partregress_grid(model, fig = fig)
plt.show()

data2 = data.select_dtypes(include=[int,float,bool])
apt_corr = data2.corr(method = 'pearson')
print(apt_corr)

apt_corr.to_csv("아파트상관계수표.csv", index=True)