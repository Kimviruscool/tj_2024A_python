# 6_부동산기술통계.py
# 부동산 실거래가 :
# 인천광역시 부평구 전월세 1년치 csv 수집

# 데이터 모델링 (그룹화)
    #전월세 기준으로 그룹해서 전용면적의 통계
# 추가
    # 부평구의 동 명을 중복 없이 출력하시오.
    # 가장 거래수가 많은 단지명을 1~5등까지 출력하시오

import json
import pandas as pd
from flask import Flask

# csv 파일을 판다스의 데이터프레임 으로 변경

#1. 데이터 read_csv 를 사용하여 csv파일 읽어오기
data = pd.read_csv('부평아파트(전월세)_실거래가.csv', encoding='utf-8', engine='python')
#2. 불러온 데이터의 이름을 재정의
data.rename(columns={'월세금(만원)':'월세금만원'} , inplace=True)
data.rename(columns={'전용면적(㎡)':'전용면적'} , inplace=True)
# print(data) #확인용

#함수 생성
def totaldata() :
    total = data.describe() #통계 #describe()

# 데이터 탐색(기술 통계)
    # 기술통계 탐색 결과를 SPRING INDEX6.HTML 테이블 형식으로 출력 (HTTP 매핑 임의로 지정)

