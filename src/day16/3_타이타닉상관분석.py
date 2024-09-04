#3_타이타닉상관분석.py
import pandas as pd
#seaborn 라이브러리 에 내장된 '타이타닉' 데이터를 가져오기
import seaborn as sns
from pandas.plotting import table

titanic = sns.load_dataset("titanic")
# print(titanic) #확인용
#호출된 타이타닉 데이터를 csv파일로 저장
titanic.to_csv('titanic.csv',index=True)
#결측 값 (누락된 값/ 공백)
print(titanic.isnull().sum()) #결측값 확인
#4. 결측값 치환, #fillna() null(결측)값 특정 값으로 채워주는 함수
    #(1) age 열의 결측값을 중앙값(크기순으로 정렬된 상태에서 중간에 위치한 값 뜻)으로 치환
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
print(titanic.isnull().sum()) #age 결측값 없어졌다.
    #(2) embarked 열의 결측값을 최빈값(집합의 빈도가 가장 많은 값) 으로 치환
    #embarked 결측값 치환
print(titanic['embarked'].value_counts())
'''
S    644
C    168
Q     77
'''
titanic['embarked'] = titanic['embarked'].fillna('S')
#embark_town 결측값 치환
print(titanic['embark_town'].value_counts())
'''
Southampton    644
Cherbourg      168
Queenstown      77
'''
titanic['embark_town'] = titanic['embark_town'].fillna("Southampton")
#deck 결측값 치환
print(titanic['deck'].value_counts())
'''
C    59
B    47
D    33
E    32
A    15
F    13
G     4
'''
titanic['deck'] = titanic['deck'].fillna("C")

#결측값 0 확인
print(titanic.isnull().sum())

print(titanic.info()) # 5. 데이터의 기본 정보
print(titanic.survived.value_counts()) # survived(생존자) 속성의 레코드 개수확인
'''
survived    생존여부
0    549    사망
1    342    생존
'''

import matplotlib.pyplot as plt
f,ax = plt.subplots(1,2, figsize = (10,5)) #서브 플롯을 이용한 한버넹 여러개 플롯 띄우기

#autopct : 원형차트내 각조각 백분율 표시 # ax = ax[0] : 첫번째 자리 #explode = [0,0.1] : 두번째 조각을 10%  정도 떨어뜨리기
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow=True)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow=True)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Survived (FeMale)')
plt.show() #남자승객 생존률은 18.9% 여자승객 생존률 74.2%

#2. (객실) 등급별 생존자 수 x축 : 등급 , hue=생존자여부(개수) # 등급별 생존자여부 개수 # data = 데이터프레임
sns.countplot(x = 'pclass',hue='survived',data=titanic)
plt.title('Pclass vs Survived')
plt.show() #생존자는 1등급 에서 가장 많고 사망자는 3등급이 가장 많다