# 3_할리스커피매장
from idlelib.iomenu import encoding

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def holly_store(result):
    for page in range(1, 51) :
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        soup = BeautifulSoup(htmlData, "html.parser")
        # print(soup)
        tbody = soup.select_one('tbody')
        for row in tbody.select('tr') :
            if len(row) <= 3: break
            tds = row.select('td')
            store_sido = tds[0].string; #print(store_sido)
            store_name = tds[1].string; #print(store_name)
            store_address = tds[3].string; #print(store_address)
            store_phone = tds[5].string; #print(store_phone)
            store = [ store_sido , store_name , store_address , store_phone]
            result.append(store) #2차원 리스트 [[], [], [], []]

def main() :
    result = []  # 할리스 매장 리스트를 여러개 저장하는 리스트 변수
    print(" >>> 할리스 매장 크롤링 중 >>>>")
    holly_store(result)
    print(result)
    hollys_tbl = pd.DataFrame(result,columns=('store','sido-gu','address','phone'))
    hollys_tbl.to_csv('hollys1.csv', encoding='cp949', mode='w',index=True)


if __name__ == "__main__" :
    main()

