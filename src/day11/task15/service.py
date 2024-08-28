#task15 > service.py
# 5_쿠우쿠우매장.py
#http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship
#1. Beautiful 이요한 쿠우쿠우 전국 매장 정보 크롤링
#2. 전국 쿠우쿠우 매장 정보 (매장특징을 제외한 모든 정보/번호,매장명,연락처,주소,영업시간)
#3. pandas 이용한 csv 파일 로 변환
#4. Flask(플라스크) 이용한 쿠우쿠우 전국 매장 정보를 반환 하는 HTTP 매핑 정의한다.
    #Http(GET) : ip주소:5000/qooqoo
    #(3)생성된 csv 파일 읽어서 json 형식을 반환
'''
1. 크롤링할 URL 확인
http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page=1
http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page=2
http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page=3
~~
http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page=6
[매개변수 파악] http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={매개변수}
2. 크롤링할 데이터 확인
    F12 관리자모드 > 데이터 위치 확인 > tbody
    1. 정보가 있는 위치 tbody
    2. <tr> 하나의 매장 정보 #홀수pc 짝수 모바일
    3. <td> 하나의 매장 각 속성 1.<td> 번호 2.지점 3.연락처 4.주소 5.영업시간
    4. 데이터 상세 위치 파악/확인
        - 번호 <td>
        - 지점명<td> ▶ <div> ▶ <a> 2번째
        - 연락처/주소/영업시간 데이터는 <td> ▶ <a>
3. Beautifulsoup 이용한 구현
'''
import json
from idlelib.iomenu import encoding

#1 모듈 가져오기
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

#쿠우쿠우 매장 정보 크롤링 서비스
def qooqooStoreInfo(result) :
    for page in range(1,7) :
        # 2 지정한 url 추출 해서 응답 받기
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = urllib.request.urlopen(url)
        if response.getcode() == 200 :
            print(">>통신 성공")
            #3. 통신 응답 결과를 읽어 와서 크롤링 파싱하기
            soup = BeautifulSoup(response.read(), "html.parser")
            #4. 분석한 HTML 식별자들을 파싱 , find/finall/select/select_one
            #4-1. 테이블 전체 파싱
            tbody = soup.select_one('tbody')
            #4-2. 테이블 마다 행 파싱
            rows = tbody.select('tr')
            #4-3. 행[매장] 마다 열 파싱
            for row in rows :
                #4-4. 열(각 매장정보) 파싱
                cols = row.select('td')
                # print(cols)
                #모바일 제외
                if len(cols) <= 1 : #만약에 열 개수가 1개이면 모바일 이라고 가정해서 파싱 제외
                    continue # 가장 가까운 반복문으로 이동, 아래 코드 실행되지 않는다.
                # 각 정보들을 파싱
                번호 = cols[0].string.strip()
                지점명 = cols[1].select('a')[1].string.strip() #두번째 열의 2개의 a태그 안에 2번째 a태그 선택(파싱)
                연락처 = cols[2].select_one('a').string.strip()
                주소 = cols[3].select_one('a').string.strip()
                영업시간 = cols[4].select_one('a').string.strip()
                #리스트 에 담기 (왜 ? DF 사용하기 위해서 2차원 리스트 구성할 예정)
                #.strip() 으로 \n,공백 제거
                매장 = [번호,지점명,연락처,주소,영업시간]
                # print(매장)
                result.append(매장) #리스트에 파싱한 리스트 담기 #2차원 리스트 구성
        else:
            print(">>통신 실패")
    #7. 리스트 반환
    return result

#[2] 2차원 리스트를 csv 반환해주는 서비스 / 데이터,CSV파일명,열(제목) 목록
def list2d_toCsv(result, fileName, colsNames) :
    try :
        #1. pandas as pd 모듈 호출
        #2. 데이터프레임 객체 생성 , 데이터 , 열 목록
        df = pd.DataFrame(result , columns=colsNames)
        #3. 데이터프레임 객체를 CSV 파일로 생성하기
        df.to_csv(f'{fileName}.csv',encoding='utf-8', mode='w')
        return True
    except Exception as e :
        print(e)
        return False

#[3] CSV 파일을 JSON형식의 py타입으로 가져오기, 가져올파일명
def read_csv_to_json(fileName):
    #1. 판다스를 이용한 CSV를 데이터프레임으로 가져오기
    df = pd.read_csv(f'{fileName}.csv', encoding='utf-8',engine='python',index_col=0)
    # index_col=0 : 판다스의 데이터프레임워크 형식 유지 (행/열 테이블 형식 )
    #2. 데이터프레임 객체를 JSON 으로 가져오기
    jsonResult = df.to_json(orient='records', force_ascii=False)
    #to_json() : 데이터프레임 객체내 데이터를 JSON 변환 함수
        #orient='records' : 각 행마다 하나의 JSON 객체로 구성
        #force_ascii=False : 아스키 문자 대신에 원래의 문자를 사용하겠다.(UTF-8) true:아스키코드사용
    #3. JSON 형식(문자열) 의 py타입(객체타입-리스트/딕셔너리)으로 변환
    reuslt = json.loads(jsonResult) #json.loads() : 문자열타입(json타입) > py타입(json형식) 변환
    return reuslt


#서비스 테스트 확인 구역
if __name__ == "__main__" :
    result = []
    qooqooStoreInfo(result) # 쿠우쿠우 매장 벙로 크롤링 서비스 호출
    # print(result)
    #매장정보를 CSV로 저장 서비스 호출
    list2d_toCsv(result, '전국쿠우쿠우매장', ['번호','지점명','연락처','주소','영업시간'] )
    result2 = read_csv_to_json('전국쿠우쿠우매장')
    print(result2)