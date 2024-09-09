#day 18 > 3_지리정보.py
import json

#주제 : 커피 매장의 주소를 이요한 지도에 마커 표시하기

#1. 데이터 준비
#pandas 모듈 호출
import pandas as pd
#csv 파일 읽어오기
df = pd.read_csv('CoffeeBean.csv', encoding='cp949', index_col=0)
#확인
print(df)
#•••231개 데이터 확인

#2. 데이터 가공 #주소 데이터를 행정구역 주소 체계에 맞게 정리 # 실습 제외
#3. 포리움 제외 #지도 시각화는 카카오 지도로 학습

from flask import Flask
app = Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route("/")
def index() :
    #df 객체를 json 변환
    jsonData = df.to_json(orient='records', force_ascii=False)
    #json 형식을 py형식으로 변환
    result = json.loads(jsonData)
    return result

if __name__ == "__main__" :
    app.run()