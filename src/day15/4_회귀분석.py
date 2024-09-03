#day15 > 4_회귀분석.py
# [1]가설 : 출석률이 좋으면 국어점수가 오른다.
# [2]주제 : 출석률에 따른 국어 점수 분석
# [3]분석방법 : #회귀분석 #출석률(원인/독립변수/연속형) ~ 국어점수(결과/종속변수/연속성)
    #1. 데이터 수집
import pandas as pd
data = pd.DataFrame({'출석률' : [80,85,90,95,70], '국어점수' : [60,65,75,80,50] })

print(data) #{열이름 : [리스트] , 열이름 : [리스트] }
    #2. 회귀 모형 수식/공식 정의 #종속변수 ~ 독립변수
RFormula = '국어점수 ~ 출석률'
    #3. 모델 피팅(해당 모형 수식을 모델에 적용해서 실행)
from statsmodels.formula.api import ols
model = ols(RFormula, data  = data).fit()
    #4. 결과
# print(model.summary()) #회귀분석 결과 요약 표 출력
print('출석률에 따른 국어점수 회귀 계수')
print(model.params) #회귀 계수 출력 #1.229730 #출석률이 1증가할 때마다 점수가 1.2 증가 한다는 예측
'''
Intercept   -37.297297
출석률           1.229730
dtype: float64
'''
print('출석률에 따른 국어점수 p값 출력')
print(model.pvalues) #p값 출력 #0.001063 #p값이 0.05 이하 이므로 가설이 효과가 있다.(유의미 하다)
'''
Intercept    0.019921
출석률          0.001063
dtype: float64
'''
print('출석률에 따른 국어점수 t통계량')
print(model.tvalues) #t통계량 출력 
'''
Intercept    -4.547357
출석률          12.660072
dtype: float64
'''
print('출석률에 따른 국어점수 표준 오차')
print(model.bse) #표준 오차
'''
Intercept    8.201972
출석률          0.097134
dtype: float64
'''

# [4]결론 및 제언 :
    #결론 : 출석률이 증가 하면 국어 점수가 증가 한다.
    #제언 : 학생들에게 출석률에 대한 이벤트 해서 국어 점수를 향상(이벤트) (활용) / 상담 (활용)

# [5] 한계점 : 결론에 따른 표본의 문제점 과 범위 설정 확인, 추후에 개발 방향성 제시