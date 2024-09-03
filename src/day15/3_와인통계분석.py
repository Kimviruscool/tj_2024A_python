# 5_와인통계분석.py
# 목표 : 와인 속성을 분석하여 품질 등급을 예측한다.
# 데이터 수집 : csv
# 데이터준비 :
# 2-1 csv파일의 열 구분자를 ; 세미콜론 > , 쉼표로 변경하여 csv 파일을 새로 만들기
import matplotlib.pyplot as plt
import pandas as pd

#새로운 csv만들기
red_pd = pd.read_csv('winequality-red.csv',sep=';',header=0,engine='python')
white_pd = pd.read_csv('winequality-white.csv',sep=';',header=0,engine='python')

red_pd.to_csv('winequality-red2.csv', index=False)
white_pd.to_csv('winequality-white2.csv', index=False)

#2-2 레드와인 과 화이트 와인 분석 하기 위해 하나로 합치기
print(red_pd.head()) # .head() 데이터프레임의 위에서부터 5개 행 출력
# 1. 열추가, # .insert(삽입할열위치,column='열이름', values=값) 0번째 첫번째 열에 type 열 이름으로 red 값들을 추가
red_pd.insert(0, column='type', value='red')
print(red_pd.head())
print(red_pd.shape) #(1599, 13) #shape : 행 개수와 열 개수 반환
print(red_pd.shape[0]) #.shape[0] : 행개수 , shape[1] : 행 개수

#2.
print(white_pd.head())
white_pd.insert(0, column='type', value='white')
print(white_pd.head())
print(white_pd.shape) #(4898, 13)
#3. 데이터 프레임 합치기 , pd.concat( [데이터프레임1, 데이터프레임2] )
wine = pd.concat([red_pd,white_pd])
print(wine.shape) #6497, 13
#4. 합친 와인 데이터 프레임을 csv로 변환
wine.to_csv('wine.csv', index=False)

#[3] 데이터 탐색
    #1. 데이터 프레임의 기존 정보 출력
print(wine.info())
    #2. 기술 통계
        # - 열이름의 공백이 있으면 _(밑줄)로 변경
wine.columns = wine.columns.str.replace(' ','_')
print(wine.head())
    #통계 #describe() : 속성(열)마다 개수, 평균, 표준편차 , 최솟값 , 백분위수 25%,50%,75%,최댓값
print(wine.describe())
print(wine.describe()['quality']) #와인의 등급 통계
print(wine.describe()['quality'].to_list()) #와인 등급의 통계 리스트
    #unique() : 중복값 제거
print(wine.quality.unique()) #[5 6 7 4 8 3 9]
print(wine['quality'].unique()) #[5 6 7 4 8 3 9]
print(sorted(wine.quality.unique() )) # 와인 등급의 중복 값 제거 하고 정렬
    #value_counts() : 특정한 열 별로 개수를 반환
print(wine.quality.value_counts())#특정한 열(등급) 별로 개수를 반환
print(wine['quality'].value_counts())#특정한 열(등급) 별로 개수를 반환
print(wine['quality'].value_counts().to_list()) #[2836, 2138, 1079, 216, 193, 30, 5] 리스트로 타입 변환
print(wine['quality'].value_counts().to_json()) #{"6":2836,"5":2138,"7":1079,"4":216,"8":193,"3":30,"9":5}

#[4]데이터 모델링
    #1. groupby('그룹기준')['속성명(quality)'] #quality 속성 기술 통계 구하기
print(wine.groupby('type')['quality'].describe())
#         count      mean       std  min  25%  50%  75%  max
# type
# red    1599.0  5.636023  0.807569  3.0  5.0  6.0  6.0  8.0
# white  4898.0  5.877909  0.885639  3.0  5.0  6.0  6.0  9.0
    #2. quality 속성의 평균
print(wine.groupby('type')['quality'].mean()) #평균만 출력
# type
# red      5.636023
# white    5.877909
# Name: quality, dtype: float64
    #3. quality 속성의 표준편차
print(wine.groupby('type')['quality'].std()) #표준편차만 출력
# type
# red      0.807569
# white    0.885639
# Name: quality, dtype: float64
    #4. type 속성으로 그룹 해서 quality 속성의 평균,표준편차 # agg 사용시 원하는 속성 여러개 가능
print(wine.groupby('type')['quality'].agg(['mean','std'])) #표준편차 , 평균 만 출력
#            mean       std
# type
# red    5.636023  0.807569
# white  5.877909  0.885639

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 24 - 09 - 03 통계 / 분석 p.209 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#[1] T-test
    #원인변수(독립변수) 레드, 화이트 (명목형)
    #결과변수(종속변수) 등급(1,2,3,4,5) (연속형)
#[1] 모듈 호출
from scipy import stats
#[2] 두 집단 표본 만들기
    #판다스 데이터프레임
    #wine (레드와인 과 화이트와인 자료를 합친 데이터 프레임 객체)
    #.loc(조건, 출력할 열)
print(wine.loc[wine['type'] == 'red','quality'])
레드와인등급집단 = wine.loc[wine['type'] == 'red' , 'quality'] #type 열의 값이 red 이면 등급 출력
화이트와인등급집단 = wine.loc[wine['type'] == 'white' , 'quality'] #type 열의 값이 white 이면 등급 출력
#[3] t-test
t통계량 , p값 = stats.ttest_ind(레드와인등급집단,화이트와인등급집단)
print(t통계량) #-9.685649554187696 # 음수는 첫번째 집단의 평균이 두번째 집단 보다 낮다. #해석 : 화이트와인 등급이 평균적으로 9.68 높다/ 차이가 있다.
print(p값)    #4.888069044201508e-22 # e-소수부 크기
if p값 < 0.05 :
    print('해당 가설은 유의미하다.')
else :
    print('해당 가설은 무의미하다.')


#2. 회귀분석 (다중 선형 회귀분석)
#[1]모듈 호출
from statsmodels.formula.api import ols #[statsmodels] 모듈설치
#[2] 회귀모형 수식(종속변수와 독립변수를 구성하는 방식/공식 : 종속변수명 ~ 독립변수1 + 독립변수2 )(p207)
회귀모형수식 = 'quality ~ alcohol' #종속변수와 독립변수를 정의 #
    #가설 : 알콜 수치에 따라 등급 확인
    #독립변수(원인/연속형) 알콜
    #종속변수(결과/연속형) 등급

    
#[3] ols(선형 회귀 모델) #ols(회귀모형수식, data = 표본집단)
선형회귀모델 = ols(회귀모형수식, data = wine)
선형회귀모델결과 = 선형회귀모델.fit() #fit() 실행
print(선형회귀모델결과.summary()) #summary() 표 형태 정리

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:                (종속변수)   R-squared:                       0.197
Model:                            OLS   Adj. R-squared:                  0.197
Method:                 Least Squares   F-statistic:                     1598.
Date:                Tue, 03 Sep 2024   Prob (F-statistic):          1.50e-312
Time:                        12:53:46   Log-Likelihood:                -7623.4
No. Observations:                6497   AIC:                         1.525e+04
Df Residuals:                    6495   BIC:                         1.526e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept(절편)         2.4053      0.086     27.988      0.000       2.237       2.574
alcohol(독립변수)        0.3253      0.008     39.970      0.000       0.309       0.341
==============================================================================
Omnibus:                      123.922   Durbin-Watson:                   1.636
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              258.800
Skew:                           0.031   Prob(JB):                     6.34e-57
Kurtosis:                       3.976   Cond. No.                         94.3
==============================================================================

   절편 : 독립변수가 0 일때 종속변수의 예측값 # X가 0일때 Y의 값
인과 관계 : 알콜 과 와인 등급 관계
                          coef    std err          t      P>|t|      [0.025      0.975]
alcohol(독립변수)        0.3253      0.008     39.970      0.000       0.309       0.341

- coef : 회귀계수
    0.3253 : 알콜 과 와인 등급 관계 해석 # 알콜이 1단위 등급 증가 할때 마다 등급 0.3253증가 한다는 예측 (알콜이 3 증가 하면 등급은 대략 1증가 한다.)
    
- std err : 표준 오차
    
- t : t검증 통계량
    
- P>|t| : t검증 p값
    0.000 : 0.05 보다 작으면 검증의 효과가 있다.
    
- [0.025      0.975] : 앞뒤 2.5% 버리고 사이에 존재 하면 신뢰할 수 있는 구간을 뜻 한다.
    
'''