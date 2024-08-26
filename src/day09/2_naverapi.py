# day09 > 2_naverapi.py
import urllib.request
from datetime import datetime
from http.client import responses
from importlib.metadata import files
from turtledemo.penrose import start
import json

NaverID = "ZL2mvZCaGouQidwZFgBJ"
NaverPW = "Sst5w27S09"

#[code 3] 매개변수로 검색대상 검색어 시작번호 한번에 표기할 개수를 받아서 url 구성하여 getRequestURL() 메소드 에게 요청하여 응답 객체를 받는다.
def getNaverSearch(node,srcText,page_start,display) :
    base = "https://openapi.naver.com/v1/search"
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&start={page_start}&display={display}'

    url = base+node+parameters #url 합치기
    print(f'>>code 3 요청 URL : {url}') #code3 확인
    #url 요청을 하고 응답받기
    responseDecode = getRequestUrl(url) #code url 요청하고 응답 객체 받기

    if responseDecode == None : return None #만약에 응답 객체가 없으면 None반환
    else : return json.loads(responseDecode) #응답 객체가 있으면 JSON 형식으로 변환
    #json.loads(문자열) : JSON 형식으로 변환 함수

#[code 4]
def getPostData(post,jsonResult,cnt) :
    #응답 받은 객체의 변수

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    #딕셔너리 생성
    dic = {'cnt' : cnt , 'title' : title , 'description' : description, 'org_link' : org_link , 'link' : org_link}
    jsonResult.append(dic)

#지정한 URL요청을 실행하고 응답을 받는 함수 [code2 ]
def getRequestUrl(url) :
    req = urllib.request.Request(url) #지정한 URL 설정
    req.add_header("X-naver-Client-Id", NaverID) ##HTTP 요청 객체내 Haeder 정보 추가
    req.add_header("X-naver-Client-Secret", NaverPW) #http요청시 네이버api id와 비밀번호 전ㄴ송

    try: #예외처리
        responses = urllib.request.urlopen(req) #지정한 url 실행후 응답 반환
        print(f'>>>code2 요청URL 결과 상태 : {responses.getcode()}') #확인
        if responses.getcode() == 200:  #만약에 응답의 상태가 200(성공) 이면 
            return responses.read().decode('utf-8') #실행된 url내 모든 내용물 읽어 오기
    except Exception as e :
        return None #없으면 None

#[code 1]
def main() :
    node = 'news' #크롤링할 대상
    srcText = input('검색어 입력하세요 : ') #검색어 입력받기
    cnt = 0 #검색 결과 개수
    jsonResult = [] # 검색 결과를 정리하여 저장할 리스트 변수
    
    #네이버 검색 결과에 대한 응답을 저장하는 객체
    #1부터 100까지의 검색 결과를 처리한다.
    jsonResponse = getNaverSearch(node,srcText, 1, 100) #[code 2]
    # total : 총 검색 결과 개수 , start 검색 시작 위치 ,display 한번에 표시 할 검색 결과 개수 , item 개별 검색 결과
    # JSON 형식의 결괏값에서는 item 속성의 JSON 배열로 개별 검색 결과를 반환합니다.

    print(f'jsonResponse : {jsonResponse}') #확인
    
    total = jsonResponse['total'] # 전체 검색 결과 개수

    #응답 객체가 None 이 아니면서 응답객체의 display 가 0이 아니면 무한반복, url응답 객체가 없을 때 까지
    while((jsonResponse != None) and (jsonResponse['display'] != 0 )) :
        # 검색결과리스트(item) 에서 하나씩 item(post) 호출
        #공문 : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4
        for post in jsonResponse['items'] : #응답받은 검색 결과 중에서 한 개를 저장한 객체
            cnt += 1 #응답 개수 변수 1 증가
            #검색 결과 한개를 처리한다.
            getPostData(post,jsonResult,cnt) #[code 3]
            
        start = jsonResponse['start'] + jsonResponse['display']
        #1, 100
        #start를 display 만큼 증가 시킨다 , 처음 요청은 1 , 100 두번째 요청은 101 , 100 세번째 요청 201 , 100
        #무료버전 기준으로 : start 1001 오류가 발생하면서 종료된다 . 1001 이상 하기 위해서는 API유료 계약 해야한다.
        jsonResponse = getNaverSearch(node,srcText,start,100) #[code 2]

    print(f'전체 검색 : {total}건')
    print(f'가져온 데이터 {cnt}건')
    # print(jsonResult)

    #Py 객체를 JSON형식의 문자열로 파일 처리
    #파일 쓰기 모드 객체 생성
    file = open(f'{srcText}-naver-{node}.json', 'w', encoding='utf-8')
    #월드컵-naver-news.json
    #json.dumps : JSON 형식의 문자열로 변환 함수
        #json.dumps(변환할Python객체, indent=들여쓰기수준4, sort_keys=알파벳순으로 정렬true/false, ensure_ascii=아스키사용여부 true/false)
        #(1) 변환할py객체 : 딕셔너리 또는 리스트 #jsonResult : 검색 결과를 정리하여 저장할 리스트 변수
        #(2) indent : 생략시 들여쓰기없음 , 주로 4정도가 많이 사용된다. / 가독성이 좋다.
        #(3) sort_keys : True(key값 기준으로 알파벳순 a-z 정렬) , false(딕셔너리 키 순서대로)
        #(4) ensure_ascii : False (UTF-8 인코딩으로 비아스키코드문자 - 주로 한글 사용시) True(기본값, 아스키코드 문자)
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

    #파일 쓰기
    file.write(jsonFile)
    #파일 닫기
    file.close()

    # #with open() as 파일변수명 : #with종료시 자동 으로 파일 닫기
    # with open(f'{srcText}-naver-{node}.json','w',encoding='utf-8) as file :
    #     jsonFile = jsondumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
    #     file.write(jsonFile)

if __name__ == "__main__" :
    main() #[code1] 메소드실행
