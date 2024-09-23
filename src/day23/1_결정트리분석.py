#1_결정트리분석.py
# 결정트리 : 로지스틱 회귀(이진분류) vs 결정트리(다중분류)
# 모델 생성 하고 예측
# [1] 데이터 수집 #데이터셋 찾는 과정
# 0. 스마트폰으로 수집한 사람의 데이터
# 1. https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones
# 2. [다운로드] UCI HAR Dataset 폴더


import numpy as np
import pandas as pd

feature_name_df = pd.read_csv("UCI_HAR_Dataset/features.txt", sep = '\s+', header = None, names = ['index','feature_name'], engine = 'python')
# sep = '\s+' : 공백 으로 구분된 csv 파일 형식
# header = None : 제목 없음
# names = ['열이름']

print(feature_name_df.head())
print(feature_name_df.shape)
#index 제거하고 feature_name 만 리스트로 저장
feature_name = feature_name_df.iloc[:,1].values.tolist()
#데이터프레임.iloc[행 슬라이싱, 열번호]
#데이터프레임.iloc[:(모든행), 1(2번째열)]
#데이터프레임.iloc[:(모든행), 1(2번째열)].values(값 추출).tolist(리스트 반환 함수)
print(feature_name[:5])

X_train = pd.read_csv('UCI_HAR_Dataset/train/X_train.txt', delim_whitespace=True, header=None, encoding='latin-1')
X_train.columns = feature_name

X_test = pd.read_csv('UCI_HAR_Dataset/test/X_test.txt', delim_whitespace=True, header=None, encoding='latin-1')
X_test.columns = feature_name

Y_train = pd.read_csv('UCI_HAR_Dataset/train/y_train.txt', sep='\s+',header=None,names=['action'], engine='python')
Y_test = pd.read_csv('UCI_HAR_Dataset/test/y_test.txt', sep='\s+',header=None,names=['action'], engine='python')

#6. 종속변수 데이터 레이블 파일 가져오기
label_name_df = pd.read_csv('UCI_HAR_Dataset/activity_labels.txt', sep='\s+',header=None,names=['index','label'], engine='python')
# 인덱스 제거 후 클래스 분류 값 리스트 추출
label_name = label_name_df.iloc[:,1].values.tolist()
print(label_name)

#데이터 수집 정리
'''
1. activity_labels.txt : 클래스(타겟,종속변수) 값에 따른 분류 값
2. feature.txt : 피처(독립변수) 값에 따른 필드(열) 이름
3. 분류된 데이터 제공 vs train_test_split
    1. 훈련용
        1. X_train.txt
        2. Y_train.txt
    2. 테스트용
        1. X_test.txt
        2. Y_test.txt
    - 변수
        1. X_train  : 독립변수 데이터프레임 (훈련용)
        2. Y_train  : 종속변수 데이터프레임
        3. X_test   : 독립변수 테스트 데이터프레임 (테스트용)
        4. Y_test   : 종속변수 테스트 데이터프레임
        5. label_name   : 종속변수 값에 따른 분류 값 , 1(걷기) 2(오르기) 3(내리기) 4(앉기) 5(서기) 6(눕기)
'''
#8. 결정트리 모델 구축하기
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier() # 결정트리 분류 분석 객체 생성
#피팅
model.fit(X_train, Y_train) #피팅 (학습)


#9. 모델 예측 (샘플 또는 테스트용 데이터 )
Y_predict = model.predict(X_test) #피팅된 모델이 새로운 데이터의 독립변수를 가지고 종속변수를 예측한다.
print(Y_predict) #[5 5 5 ... 2 1 2] #독립변수를 넣고 예측한 종속변수 들

#10. 모델의 정확도 예측
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test, Y_predict) #정확도 확인 #실제값(y_test) , 예측(y_predict)
print(accuracy) #0.8598574821852731 #1에 가까울 수록 예측을 잘 하고 있다.
# * 결정트리 모델 시각화
import matplotlib.pyplot as plt
from sklearn import tree
tree.plot_tree(model, feature_names=feature_name, class_names=label_name)
#tree.plot_tree(결정트리모델객체, feature_names=[피처이름들], class_names=[클래스레이블들])
plt.show()

#11. (모델의 성능 개선) 최적의 하이퍼 매개변수 찾기 #최적의 정확도가 높은 트리의 찾기 # 정확도가 가장 높았을 때의 매개변수를 찾아보자
#(1) 결정 트리가 사용하는 하이퍼 매개변수 종류
print(model.get_params())
    #depth : 트리의 깊이 #max_depth : 최대 트리의 깊이
    #criterion : 노드 결정 방식

from sklearn.model_selection import GridSearchCV
# (2) 최적의 하이퍼 매개변수를 찾을 설정값을 변수 만들기
'''
params = {
    'max_depth' : [6,8,10,12,16,20,24]
}
# (3) 다양한 하이퍼파라미터 조합을 시도해서 최적의 하이퍼 파라미터를 찾는데 사용되는 도구/함수 모듈 , 교차 검증 제공
#객체 생성
#미리 설정한 'params'의 'max_depth'라는 최대 노드 깊이를 (5회)교차 검증하는 cv객체
grid_cv = GridSearchCV(model,param_grid=params,scoring='accuracy',cv=5,return_train_score=True)
#GridSearchCV(model,param_grid=params,scoring='accuracy',cv=5,return_train_score=True)
#GridSearchCV(확인할 트리 모델 객체, param_grid = 테스트할 설정변수 , scoring='정확도', cv=교차횟수)
    #cv = 5 #교차 검증 #데이터를 5개로 나누어서 5번 반복해서 모델 학습
    # return_train_score : 검증후 정수도 같이 반환 하겠다 라는 뜻을 가진 속성
    # scoring='accuracy' : 모델 평가 기준을 정확도 기준으로 하겠다는 뜻을 가진 속성
# cv 객체 테스트 (피팅)
grid_cv.fit(X_train,Y_train)
print(grid_cv.cv_results_)
cv_reesults_df = pd.DataFrame(grid_cv.cv_results_)

cv_reesults_df[['param_max_depth', 'mean_test_score', 'mean_train_score']]

print(f'최고 평균 정확도 : {grid_cv.best_score_}, 최적 하이퍼 매개변수 : {grid_cv.best_params_}')
# 최고 평균 정확도 : 0.85174886814005, 최적 하이퍼 매개변수 : {'max_depth': 8}
# 사용처 : 다음에 모델 만들때 최적의 하이퍼 매개변수를 사용
# model = DecisionTreeClassifier( max_depth = 16(최적의 파라미터 값) )
'''
#12 모델의 성능 개선 최적의 하이퍼 파라미터 찾기2
params = {
    'max_depth' : [8,16,20],
    'min_samples_split' : [8,16,24]
}

grid_cv = GridSearchCV(model,param_grid=params,scoring='accuracy',cv=5,return_train_score=True)
grid_cv.fit(X_train,Y_train)
cv_reesults_df = pd.DataFrame(grid_cv.cv_results_)
cv_reesults_df[['param_max_depth','param_min_samples_split','mean_test_score','mean_train_score']]

print(f'최고 평균 정확도1 : {grid_cv.best_score_}, 최적 하이퍼 매개변수1 : {grid_cv.best_params_}')
#최고 평균 정확도1 : 0.8541972002941218, 최적 하이퍼 매개변수1 : {'max_depth': 8, 'min_samples_split': 8}

model2 = DecisionTreeClassifier(max_depth=8, min_samples_split=8)
model2.fit(X_train, Y_train)
Y_predict2 = model2.predict(X_test)
ac = accuracy_score(Y_test, Y_predict2)
print(ac)

tree.plot_tree(model2, feature_names=feature_name, class_names=label_name)
#tree.plot_tree(결정트리모델객체, feature_names=[피처이름들], class_names=[클래스레이블들])
plt.show()