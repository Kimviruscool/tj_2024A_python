#[1] 데이터 수집
import pandas as pd
data = pd.DataFrame({
    '운동시간': [1, 2, 3, 4, 5, 2, 3, 4, 5, 6,
                1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
    '게임시간': [2, 3, 4, 5, 6, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
    '체중': [60, 62, 64, 66, 68, 65, 67, 69, 71, 73,
            62, 64, 66, 68, 70, 64, 66, 68, 70, 72]
})
#[2] 데이터 통계분석 #운동시간에 따른 체중 변화 비교
    #1. 모형 수식 정의
Rformula ='체중 ~ 운동시간 + 게임시간'
    #2. 모델 피팅
from statsmodels.formula.api import ols
model = ols(Rformula, data = data ).fit()
    # 모델 결과 확인
print(model.params) #회귀계수
'''
Intercept    38.722222
운동시간        -18.277778 # 평균적으로 운동시간이 1시간 마다 체중이 18.27 감소 한다.
게임시간         20.444444 # 평균적으로 게임시간이 1시간 마다 체중은 20.44 증가 한다.
dtype: float64
'''

print(model.pvalues) #p값
'''
Intercept    1.404150e-24
운동시간         6.968463e-22 #p값이 0.05이하 이므로 귀무가설 기각 할수 있다.
게임시간         5.508640e-28 #p값이 0.05이하 이므로 귀무가설 기각 할수 있다.
dtype: float64
'''
#[3] 학습된 모델 기준으로 새로운 샘플 체중을 예측하자. #운동시간과 게임시간을 알고 있는 상태에서 체중 예측하기
sampleData = pd.DataFrame({'운동시간' : [0,4,2], '게임시간' : [2,5,4]})
print(sampleData) #예측 전
# ~~ [2] 에서 학습된 모델을 이용한 예측 수행 #모델객체.prdict(새로운샘플)
samplePrediction = model.predict(sampleData)
print(samplePrediction) #샘플의 예측값
'''
0    79.611111
1    67.833333
2    83.944444
'''
