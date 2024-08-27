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

result = []

for page in range(1,7) :
    url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
    response = urllib.request.urlopen(url)
    htmlData = response.read()
    soup = BeautifulSoup(htmlData,"html.parser")

    # print(soup.select('.td-mobile'))

    tbody = soup.select_one('tbody')
    for tr in tbody.select('tr') :
      td = tr.select('td')


    #
    # tbody = soup.select_one("tbody")
    # tr = tbody.select("tr")
    # # print(tr[0].text)
    # for i in tr :
    #     print(i.text)

# print(result)
