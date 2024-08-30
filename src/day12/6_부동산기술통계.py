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
from idlelib.iomenu import encoding

import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask #[1]플라스크 모듈 호출

app = Flask(__name__)#[2] 플라스크 객체 만들기
#[*] CORS 허용
from flask_cors import CORS
CORS(app)



#[4] 플라스크 HTTP 매핑 정의
#1.
@app.route("/trans1", methods=["GET"])
def trans1():
    return json.loads(df.describe().to_json())
#2.
@app.route("/trans2", methods=['get'])
def trans2():
    return json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json())
#3.
@app.route("/trans3", methods=['get'])
def trans3():
    return list(df['시군구'].unique())
#4.
@app.route("/trans4", methods=['get'])
def trans4():
    return json.loads(df['단지명'].value_counts().head().to_json())

#csv 호출 후 새로운 csv 만들기 
df1 = pd.read_csv('아파트(전월세)_실거래가_2022-2023.csv', encoding='utf-8', engine='python', skiprows=15)

df2 = pd.read_csv('아파트(전월세)_실거래가_2023-2024.csv', encoding='utf-8', engine='python', skiprows=15)

df3 = pd.read_csv('아파트(전월세)_실거래가_2024-today.csv', encoding='utf-8', engine='python', skiprows=15)

totalAptData = pd.concat([df1,df2,df3])
# print(totalAptData.shape) #37034 1
totalAptData.to_csv('Apttotal.csv', mode='w', encoding='utf-8', index=False)

#[***]
df = pd.DataFrame()
for year in range (2022,2025) :
    df2 = pd.read_csv(f'{year}.csv', encoding='cp949', skiprows=15)
    print(df2.shape) #shape. 레코드수, 열개수 확인
    df = pd.concat([df,df2])

# print(f'totalAptdata >>> {totalAptData}')

df = pd.read_csv('Apttotal.csv', encoding='utf-8', engine='python', skiprows='0')
#encoding='utf-8'이 안될시 cp949
#skiprows='' : 특정 행을 제외하고 csv 읽어오기
# print(df)
#1. describe() : 통계
# print(df.describe()) #count(개수) , mean(평균), std(편차), min(최솟값), max(최댓값), 25%,50%,70%(백분위수)
# print(df.describe().to_json) #통계 json형식의 문자열로 변경
print(json.loads(df.describe().to_json())) # json 문자열 타입 > (dic 딕셔너리)py타입으로 변경 # 플라스크 HTTP응답시 전송하기 위해서

#2. 그룹화 통계
# print(json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json()))
print(json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json())) #json 타입으로 그룹화 하여 통계 데이터 읽어오기

#3. '시군구' 출력 , 중복제거
# print(df['시군구'])
print(df['시군구'].unique())

#4. 단지명 출력 , 레코드 수
# print(df['단지명'].unique()) #unique() : 중복제거
# print(df['단지명'].value_counts()) #value_counts() : df 에서 특정 열의 레코드(행) 수 출력
# print(df['단지명'].value_counts().head()) #df 에서 위에서 5개만 추출 = .head()
print(json.loads(df['단지명'].value_counts().head().to_json()))

#[3] 플라스크 실행 (순차 실행 맨 아래 실행 함수 생성)
if __name__ == "__main__" :
    app.run(host='0.0.0.0' , debug=True)
    #host = '0.0.0.0' #다른사람 접속 허용
    #debug = True 오류 잡아주기