# 5_쿠우쿠우매장.py
#http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship
#1. Beautiful 이요한 쿠우쿠우 전국 매장 정보 크롤링
#2. 전국 쿠우쿠우 매장 정보 (매장특징을 제외한 모든 정보/번호,매장명,연락처,주소,영업시간)
#3. pandas 이용한 csv 파일 로 변환
#4. Flask(플라스크) 이용한 쿠우쿠우 전국 매장 정보를 반환 하는 HTTP 매핑 정의한다.
    #Http(GET) : 포트:5000/qooqoo
    #(3)생성된 csv 파일 읽어서 json 형식을 반환

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask


def qooqoo(result) :
    for page in range(1,7) :
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        soup = BeautifulSoup(htmlData,"html.parser")
        tbody = soup.select_one('tbody')
        for row in tbody.select('tr') :
            tds = row.select('td')
            if len(tds) < 5: continue
            num = tds[0].text.strip() #print(num)
            name = tds[1].select('a')[1].text.strip() #print(name)
            phone = tds[2].text.strip() #print(phone)
            address = tds[3].text.strip() #print(address)
            time = tds[4].text.strip() #print(time)
            store = [ num , name , phone , address , time]
            result.append(store)

def main():
    result = []
    print(">>>> 쿠우쿠우 크롤링 >>>>")
    qooqoo(result)
    tb1 = pd.DataFrame(result, columns=('num','name','phone','address','time'))
    tb1.to_csv("qooqoo.csv",mode='w',index=False)

    return result

app = Flask(__name__)

@app.route('/')
def index() : # 매핑 함수
    result = main()
    return result


if __name__ == '__main__' :
    app.run( debug=True )