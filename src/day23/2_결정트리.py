#2.결정트리.py
# 어종 데이터셋 : https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv
# 주제 : 여러 어종의 특성 들을 바탕으로 어종명 예측하기
#Species 종류 ,Weight 크기 ,Length 길이 ,Diagonal 대각선길이 ,Height 높이 ,Width 넓이

#[1] 데이터 셋
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv')
# print(df.head()) #확인

#[2] 7:3 비율로 훈련용 테스트용으로 분리 하기
x = df[['Weight','Length','Diagonal','Height',"Width"]]#피처
# print(x)
y= df['Species']#타겟
# print(y)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier() #모델 생성
from sklearn.model_selection import train_test_split, GridSearchCV

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=0)

#[3] 결정트리 모델로 훈련용 데이터 피팅하기
model.fit(x_train,y_train) #피팅

#[4] 훈련된 모델 기반으로 테스트용 데이터 예측하고 정확도 확인하기 (accuracy_score)
#출력예시 ] 개선 전 결정트리모델 정확도 : 0.625
y_predict = model.predict(x_test)
# print(y_predict)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_predict)

print(accuracy) #0.625

#[5] 최적의 하이퍼 파라미터 찾기 # params = {'max_depth' : [2,6,10,14],'min_samples_split':[2,4,6,8]}
#출력예시 ] 평균 정확도 : 0.xxxxxxx 최적 하이퍼파라미터 : {'max_depth' : xx , 'min_samples_split': x}
params = {
    'max_depth' : [2,6,10,14],
    'min_samples_split' : [2,6,4,8]
}

grid_cv = GridSearchCV(model,param_grid=params,scoring='accuracy', cv=5, return_train_score=True)
grid_cv.fit(x_train, y_train)
cv_result_df = pd.DataFrame(grid_cv.cv_results_)
cv_result_df[['param_max_depth','mean_test_score','mean_train_score']]

print(f'평균 정확도 : {grid_cv.best_score_} , 최적 하이퍼 파라미터 : {grid_cv.best_params_}')
#평균 정확도 : 0.7209486166007905 , 최적 하이퍼 파라미터 : {'max_depth': 10, 'min_samples_split': 2}

#[6] 최적의 하이퍼 파라미터 기반으로 모델 개선후 테스트용 데이터 예측하고 예측 정확도 확인하기 #시각화 하기
#출력예시 ] 개선 후 결정트리 모델 정확도 : 0.xxxxxx
#차트 시각화
import matplotlib.pyplot as plt
from sklearn import tree

model2 = DecisionTreeClassifier(max_depth=10, min_samples_split=2)
model2.fit(x_train, y_train)
y_predict2 = model2.predict(x_test)
ac = accuracy_score(y_test, y_predict2)
print(ac)


tree.plot_tree(model2, feature_names=['Weight','Length','Diagonal','Height','Width'], class_names=['Bream','Roach','Whitefish','Parkki','Perch','Pike','Smelt'])
plt.show()