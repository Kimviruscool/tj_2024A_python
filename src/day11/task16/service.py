'''
- task16 : 잡코리아의 [java]검색 크롤링 서비스 구축
- 기본링크 : https://www.jobkorea.co.kr/Search/?stext=java
- [java] 검색결과의 모든 채용공고를 크롤링 서비스 만들기
- 채용공고 정보 파싱 : 회사명 , 공고명 , 경력 , 학력 , 계약유형 , 지역 , 채용기간
- [조건1] 페이지수를 계산 : 총 채용공고수 , 페이지당 공고수  활용 하여 계산
- [조건2] 크롤링 한 결과를 CSV 변환 서비스
- [조건3] CSV 파일을 JSON 변환 서비스
- [조건4] Spring : index5.html , py : task16 > appstart.py , service.py , controller.py 파일만 사용.

[ 기능구현 ]
[1] [java]검색결과의 모든 채용공고를 spring web html에 테이블 에 출력하시오.
--------------------------------------------------------------
[2] [PY 서비스추가] 총채용공고수 , 경력별 공고수 , 학력별 공고수 를 [1]번 테이블 위에 출력 하시오.
--------------------------------------------------------------
[3] html 에서 input 박스로 검색어를 입력 받아 검색 버튼을 클릭했을때 입력받은 값으로 검색결과를 서비스 제공 하기.

전체 박스 class = "list"
회사명 class = "list" > div > a.string
공고명 class = "list" > div > a.string
경력 class = "list" > div > ul > li[0]
학력 class = "list" > div > ul > li[1]
계약유형 class = "list" > div > ul > li[2]
지역 class = "list" > div > ul > li[3]
채용기간 class = "list" > div > ul > li[4]
'''
from itertools import count

# 1. 모듈 가져오기
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json

def getJobInfo(result):
    for page in range(1 , 2):
        print(f'>>> page : {page}')
        url = f"https://www.jobkorea.co.kr/Search/?stext=java&Page_No={page}"
        reponse = urllib.request.urlopen(url)
        if reponse.getcode() == 200:
            print(">>> 통신 성공")
            # 3. 통신한 결과를 읽어와서 크롤링 파싱하기
            soup = BeautifulSoup(reponse.read(), "html.parser");  # print(soup)
            # 4. 분석한 HTML 식별자들을 파싱 , find , findAll , select , select_one
            aticle = soup.select_one(".list");   # print(aticle)  # 4-1 테이블 전체 파싱
            # print(f'>>> aticle : {aticle}')
            for row in aticle.select(".list-item"):
                # print(f'>>> row : {row}')
                companyName = row.select("div")[0].select_one('a').string.strip(); # print(f'>>> companyName : {companyName}')
                announcementName = row.select("div")[1].select_one('a').text.strip(); # print(f'>>> announcementName : {announcementName}')
                listInfo = row.select("div")[1].select_one('ul')
                # print(f'listInfo : {len(listInfo)}')
                chipInfoGroup = []
                chipInfo = listInfo.text
                # print(chipInfo)
                for string in chipInfo.split("\n")[1:-1]:
                    chipInfoGroup.append(string)
                # print(chipInfoGroup)
                # personalHistory = listInfo[0].string.strip(); # print(f'>>> personalHistory : {personalHistory}')
                # education = listInfo[1].string.strip(); # print(f'>>> education : {education}')
                # contractType = listInfo[2].string.strip(); # print(f'>>> contractType : {contractType}')
                # region = listInfo[3].string.strip(); # print(f'>>> region : {region}')
                # period = listInfo[4].string.strip(); # print(f'>>> period : {period}')
                jobInfo = [companyName, announcementName, chipInfoGroup];  # (f'>>> jobInfo : {jobInfo}')
                result.append(jobInfo)

        else:
            print(">>> 통신 실패")
    # print(f'result : {result}')
    return result

def list2d_to_csv(result , fileName , colsNames):
    try:
        # 1. import pandas as pd 모듈 호출한다.
        # 2. 데이터 프레임 객체 생성 , 데이터 , 열 목록
        df = pd.DataFrame(result , columns=colsNames)
        # print(df)
        # 3. 데이터 프레임 객체를 csv 파일로 생성하기
        df.to_csv(f'{fileName}.csv' , encoding='utf-8' , mode='w')
        return True
    except Exception as e:
        print(f">>> e : {e}")
        return False

def read_csv_to_json(fileName):
    # 1. 판다스를 이용한 csv를 데이터 프레임으로 가져오기
    df = pd.read_csv(f'{fileName}.csv' , encoding='utf-8' , engine='python' , index_col=0)
        # index_col=0 : 판다스의 데이터프레임 형식 유지(테이블형식)
    # 2. 데이터프레임 객체를 json으로 가져오기
    jsonResult = df.to_json(orient='records' , force_ascii=False)
        # .to_json() : 데이터프레임 객체내 데이터를 json 변환함수
            # orient='records' : 각 행마다 하나의 json 객체로 구성
            # force_ascii=False : 아스키 문자 사용 여부 : True (아스키코드사용) , False(유니코드 utf-8사용)
    # 3. json 형식(문자열)의 py타입(객체타입 - 리스트/딕셔너리)으로 변환
    result = json.loads(jsonResult)    # json.loads() 문자열타입(json형식) ---> py타입(json형식) 변환
    # print( result )
    for r in result:
        print( r )
        r['기타'] = eval(r['기타']) # 2차원 리스트 안에 있는거까지 변환을 못해줌 그래서 eval() 함수
    # print(result)
    return result

# [2] [PY 서비스추가] 총채용공고수 , 경력별 공고수 , 학력별 공고수 를 [1]번 테이블 위에 출력 하시오.
def totalJobInfo(result2):
    total = str(len(result2))
    return total


def newhistory(result2):
    new = result2.count("신입")
    return new

# if __name__ == "__main__":
#     result = []
#     getJobInfo(result)
#     list2d_to_csv(result, 'jobInfo', ['회사명', '공고명', '기타'])  # 매장정보를 csv로 저장 서비스 호출
#     # newhistory(result)
#     result2 = read_csv_to_json('jobInfo')
#     result3 = newhistory('jobInfo')
#     # print(result2)
#     print(result3.select_one('기타'))
