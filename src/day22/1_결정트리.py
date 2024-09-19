#1_결정트리.py
'''
1. 분류분석
    1. 로지스틱 회귀 분석 : 이진 분류
    2. 결정트리 분석 : 주로 다중 분류
        - 피처 , 독립변수
        - 클래스 , 타겟 , 종속변수
2. 결정트리란?
    - 트리 구조 기반으로 의사를 결정 해서 조건을 나타내고 최종적인 리프노드 로 결과를 제공
        종류
        - 루트노드 : 트리 최상단 위치
        - 내부/규칙 노드 : 속성(특징)에 기반해 데이터를 분할 하는 기준 되는 노드
        - 리프 노드 : 더 이상 분할 되지 않고 최종적인 결과 노드
        노드 선택 기준
        1. 엔트로피 : 정보이득지수(엔트로피가 줄어 들어 얻게 되는 이득)가 높은 피처를 분할 기준으로 사용 # DecisionTreeClassifier(criterion='entropy') : 엔트로피
            - 예] 주스를 생상하는데 사과와 오렌지를 섞어서 쥬스 만드는데 섞인 주스의 맛이 얼마나 (혼잡)(혼란) 스러운지 측정하는 것이 엔트로피 입니디ㅏ.
                - 주스에 사과 와 오렌지가 섞여서 맛이 햇갈릴때 혼잡도가 높다., 엔트로피가 높다
                - 주스에 사과 또는 오렌지 맛만 느껴질때 , 혼잡이 낮다 , 엔트로피가 낮다.
            - 즉 ] 불확실성을 측정하는 지표로 값이 낮을수록 분류가 잘 된다는 것을 의미

        2. 지니 계수 : 지니 계수가 낮은 피터를 기준으로 기준으로 사용 # DecisionTreeClassifier(criterion='gini') : 기본값
            - 주스에 사과 와 오렌지가 섞여서 맛이 헷가릴때 예측이 어렵다. 지니 계수가 높다.
            - 주스에 사과 또는 오렌지 맛만 느껴질때 , 예측이 쉽다 . 지니 계수가 낮다.
        - 즉 ] 분순도를 측정하는 지표로 값이 낮을수록 분류가 잘 된다는 것을 의미
'''

#[1] 데이터 샘플
data = {
    'size': [1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 2, 1, 3, 1, 2],  # 과일의 크기
    'color': [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3, 3],  # 1: 빨간색, 2: 주황색, 3: 노란색
    'labels': [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 1, 0, 2, 2]  # 0: 사과, 1: 오렌지, 2: 바나나
}
#[2] 데이터 프레임
import pandas as pd
df = pd.DataFrame(data)
print(df)

#[3] 독립변수(피처) 종속변수(타겟/클래스) 나누기
x = df[['size','color']] #피처
print(x)

y = df['labels'] #타겟
print(y)

#[4] 결정 트리 모델 생성 #DecisionTreeClassifier(criterion= 'gini : 기본값 ' , 'entropy : 엔트로피 방식')
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy')

#[8] 훈련용 , 테스트용 나누기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#[5] 모델 피팅
model.fit(x_train,y_train)

#[8] 예측
y_pred = model.predict(x_test)
print(y_pred) # [1,2,2]
#[9] 정확도 #accuracy_score
from sklearn.metrics import accuracy_score #정확도 함수
accuracy = accuracy_score(y_test , y_pred) #실제값  , 예측값 입력 : 정확도확인

print(accuracy) #0.6666666666666666

#[6] 확인
print(model.get_depth()) #depth() : 트리의 깊이 #2
print(model.get_n_leaves()) #get_n_leaves() : 노드의 개수 #3
#[7] 시각화
import matplotlib.pyplot as plt
from sklearn import tree
tree.plot_tree(model, feature_names=['size','color'],class_names=['apple','orange','banana'])
plt.show()