# 3_tourApi.py
# 공공데이터포털 : https://www.data.go.kr/index.do > 로그인
# 출입국관광통계서비스 검색 (한국문화관광연구원_출입국관광통계서비스)
# 활용신청
import urllib.request
import json
from calendar import month



#[Code 4]
def getTourismStateService(nat_cd,ed_cd,nStartYear,nEndYear):
    jsonResult = [] #수집한 데이터를 저장할 리스트 객체
    dataEnd = f'{str(nEndYear)}{str(12)}' #마지막 연도의 마지막 월 (12)
    isDataEnd = 0 #데이터의 끝 확인하는 함수
    for year in range(nStartYear, nEndYear+1 ) : #시작연도 부터 끝연도 까지 반복 for문
        print(f">>year : {year}")
        for month in range(1,13) : #1 ~ 13(미만), 1~12월까지 반복
            print(f">>>month : {month}")
            if isDataEnd == 1 : break #만약에 isDataEnd가 1이면 반복문 종료
            # :0>2 오른쪽 정렬 > , 2(자릿수) , 0 (빈칸이면 0채움) # 1>01,10>10,5>05
            yyyymm = f'{str(year)}{str(month):0>2}'
            jsonData = getTourismStatesItem(yyyymm , nat_cd, ed_cd)
            if jsonData != None :
                print(jsonData)
                if jsonData['response']['body']['items'] == '' :
                    isDataEnd = 1 #지정한 날짜에 내용물이 없으므로 반복문 종료
                    print('>>> 데이터 없음')
                    break
                #아니고 내용물이 있으면
                natName = jsonData['response']['body']['items']['item']['natKorNm'] #국가명
                natName = natName.replace(' ','')#공백제거
                num =  jsonData['response']['body']['items']['item']['num'] #관광객 수
                #딕셔너리
                dic = {'nat_Name' : natName , 'nat_cd' : nat_cd , 'yyyymm' : yyyymm , 'visit_cnt' : num }
                jsonResult.append(dic) #딕셔너리를 리스트에 담기
    #모든 반복문 종료후
    return jsonResult

ServiceKey = "nwPZ%2F9Z3sVtcxGNXxOZfOXwnivybRXYmyoIDyvU%2BVDssxywHNMU2tA55Xa8zvHWK0bninVkiuZAA4550BDqIbQ%3D%3D"
#[Code 3] 지정한 날짜 , 지정한 국가 , 구분을 받아서 url 요청하기
def getTourismStatesItem(yyyymm,nat_cd,ed_cd):
    #1. 출입국관광통계 의 기본 URL
    base = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    #2. 인증키 , 년월, 국가코드, 출입국 구분 코드
    parameters = f'?_type=json&serviceKey={ServiceKey}'
    parameters += f'&YM={yyyymm}'
    parameters += f'&NAT_CD={nat_cd}'
    parameters += f'&ED_CD={ed_cd}'
    #3. 합치기
    url = base+parameters
    print(f'>>>url : {url}')
    #url 요청후 응답객체 받기
    responsesDecode = getRequestUrl(url)
    if (responsesDecode == None) : #만약에 응답객체가 None 이면 None 반환
        return None
    else : #만약에 응답객체가 존재하면 json형식을 파이썬 객체로 반환 함수
        return json.loads(responsesDecode)
    #json.loads() JSON형식 > py형식 , json,dumps()PY형식 > json형식 함수
    #JS : JSON.parse() JSON형식 > JS형식 변환 함수 , JSON.stringfy() JS형식 > JSON형식 변환 함수


#[Code 2]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e :
        return None

#[Code 1]
def main() :

    nat_cd = int(input("국가코드[ 중국(112)/일본(130)/미국(275) ] : ")) #2. 국가코드 (공문참고)
    nStartYear = int(input('시작 연도 : ')) #3. 데이터 수집 시작 연도
    nEndYear = int(input('끝 연도 : ')) #4 마지막 데이터의 연도
    ed_cd = 'E' # 5. 구분(E :방한외래관광객(입국) , D : 해외 출국)

    jsonResult = [] # 1. 수집한 데이터를 저장할 리스트 객체 생성
    jsonResult = getTourismStateService(nat_cd,ed_cd,nStartYear,nEndYear) #6. 서비스 요청후 응답 객체 받기
    print(jsonResult) #확인

    #7. 응답받은 py객체를 json 으로 변환후 파일처리
    with open(f'{nat_cd}-{nStartYear}-{nEndYear}.json', 'w', encoding='utf-8' ) as file :
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)

if __name__ == "__main__" :
    main()
