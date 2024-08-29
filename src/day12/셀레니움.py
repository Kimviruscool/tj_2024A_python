# 셀레니움.py
# 1. 모듈 가져오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

#[1] 커피빈 정적 크롤링 함수
def CoffeBean_Store(result) :
    #2. webdriver객체 생성
    wd = webdriver.Chrome()

    #3 .webdriver 객체를 이용한 웹페에지 접속, .get(URL)
    # wd.get("http//www.hanbit.co.kr")
    for i in range(1,10) : #시간상 1~9 까지만

        #실습 : 커피빈 매장 정보(동적페이지 = JS이벤트) 크롤링

        #1. 커피빈 웹페이지 연결
        wd.get("https://www.coffeebeankorea.com/store/store.asp")
        time.sleep(2) #2초 일시정지 (대기상태) #웹페이지가 열릴때까지 2초 대기 #컴퓨터마다 다를수있음

        try :
            #2. 커피빈 웹페이지 자바 스크립트 함수 호출,
            wd.execute_script(f"storePop2({i})")
            time.sleep(2) #2초 일시정지 (대기상태)

            #3. 자바스크립트 함수가 수행된 페이지의 소스 코드를 저장
            html = wd.page_source
            #4. Beautiful 객체 생성
            soupCB1 = BeautifulSoup(html,'html.parser')
            # print(soupCB1.prettify())

            #6. 특정 매장 정보의 모달창에서 매장 정보 파싱하기
            store_name_h2 = soupCB1.select('div.store_txt >h2')
            # print(store_name_h2) #[<h2>부평문화의거리점</h2>]

            store_name = store_name_h2[0].string
            # print(store_name) #부평문화의거리점

            store_info = soupCB1.select('.store_txt>table.store_table>tbody>tr>td')
            # print(store_info) #[<td>월-목 09:00-23:00 | 금-토 09:00-24:00 | 일 09:00-23:00</td>, <td>주차불가</td>, <td>인천광역시 부평구 시장로29 1,2층  <!--span class="lot">(인천광역시 부평구 시장로29 1,2층)</span--></td>, <td>032-507-9901</td>]

            store_address_list = list(store_info[2]) #['인천광역시 부평구 시장로29 1,2층  ', 'span class="lot">(인천광역시 부평구 시장로29 1,2층)</span']
            store_address = store_address_list[0]
            # print(store_address) #인천광역시 부평구 시장로29 1,2층

            store_phone = store_info[3].string
            # print(store_phone) #032-507-9901

            #매장 정보의 리스트 선언
            store = [store_name,store_address,store_phone]
            #매장 정보 리스트를 매장리스트에 담기, 2차원 리스트
            result.append(store)

        except Exception as e :
            print(e)
    #for end
    return result

def main() :
    result = []
    CoffeBean_Store(result)
    print(result)
    #판다스를 이용한 2차원 리스트를 데이터 프레임 객체 생성
    CB_tbl = pd.DataFrame(result, columns=['store','address','phone'])
    #데이터프레임 객체 정보를 CSV 파일로 변환
    CB_tbl.to_csv("coffeBean.csv",encoding='utf-8', mode='w',index=True)

if __name__ == "__main__" :
    main()