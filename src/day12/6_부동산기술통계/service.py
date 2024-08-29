# 6_부동산기술통계.py
# 부동산 실거래가 :
# 인천광역시 부평구 전월세 1년치 csv 수집
# csv 파일을 판다스의 데이터프레임 으로 변경
# 데이터 탐색(기술 통계)
    # 기술통계 탐색 결과를 SPRING INDEX6.HTML 테이블 형식으로 출력 (HTTP 매핑 임의로 지정)
# 데이터 모델링 (그룹화)
    #전월세 기준으로 그룹해서 전용면적의 통계
# 추가
    # 부평구의 동 명을 중복 없이 출력하시오.
    # 가장 거래수가 많은 단지명을 1~5등까지 출력하시오

import json
import pandas as pd
import matplotlib.pyplot as plt
def readapt(fileName):
    df = pd.read_csv(f'{fileName}.csv', encoding='utf-8', engine='python')
    # print(df)
    jsonResult = df.to_json(orient='records', force_ascii=False)
    result = json.loads(jsonResult)
    return result