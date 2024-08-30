# day12 > 과제 > 과제.py
"""
    Spring: index7.html 사용, flask 이용한 Spring 통신
    1. 데이터 전체 출력(~10000개)
    2. 기술통계 이용한 계산 4개 출력
"""
from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

df = pd.read_csv("워싱턴주_전기차.csv", encoding='cp949')


# 전체 데이터 10000행
@app.route("/vehicle")
def vehicle():
    # 데이터프레임 객체의 상위 행 1000개를 행 기준으로 JSON화한 다음 JSON객체로 반환
    return json.loads(df.head(1000).to_json(orient="records"))


# 전기차 주행거리
@app.route("/vehiclemile")
def vehicle_mile():
    # df[df 조건문] = df 필터링된 결과: df[df["주행거리"] != 0] => 주행거리 열에서 0 값을 제외한 행만으로 필터링
    return json.loads(round(df[df["주행거리"] != 0]["주행거리"].describe(), 2).to_json())


# 전기차 브랜드별 레코드 갯수
@app.route("/vehiclemakes")
def vehicle_makes():
    # df.value_counts(): 각 값의 갯수를 세서 Series로 반환
    # to_json(orient="split") = 인덱스 목록과 값 목록을 각각 리스트로 나누어 반환
    return json.loads(df["브랜드"].value_counts().head(10).to_json(orient="split"))


# 차량 출시연도 기술통계
@app.route("/vehicleyear")
def vehicle_year():
    return json.loads(df["연식"].describe().to_json(force_ascii=False))


# MSRP 소비자가격
@app.route("/vehicleprice")
def vehicle_price():
    return json.loads(df[df["권장소비자가격"] != 0]["권장소비자가격"].describe().to_json(force_ascii=False))


# 전기차 방식
@app.route("/vehicletype")
def vehicle_type():
    result = []
    result.append(df["전기차종류"].value_counts().tolist())
    # .value_counts(normalize=True): 백분율, *100 / .tolist(): 리스트로 반환
    result.append(round((df["전기차종류"].value_counts(normalize=True)*100), 1).tolist())
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
