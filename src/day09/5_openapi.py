# 5_openapi.py
import urllib.request
from http.client import responses

from flask import request
import json

#연습문제 : 서울 열린데이터 광장에서 '민주주의 서울 자유제안'을 크롤링하여 JSON파일로 저장하시오.
# url :  http://openapi.seoul.go.kr:8088/인증키/xml/ChunmanFreeSuggestions/1(시작번호)/5(데이터 수)/%EB%84%88%EB%AC%B4(검색어)


# [Code 4]
def getSeoulService(start_num,end_num):
    jsonResult = []
    isDataEnd = 0

    jsonData = getSeoulItem(start_num,end_num)
    if jsonData != None :
        print(jsonData)
        for item in jsonData['ChunmanFreeSuggestions']['row'] :
            SN = item['SN']
            TITLE = item['TITLE']
            content = item['content']
            REG_DATE = item['REG_DATE']

            dic = {'SN' : SN, 'TITLE' : TITLE, 'content' : content, 'REG_DATE' : REG_DATE }
            jsonResult.append(dic)
    else :
        return
    return jsonResult

Itemkey = "4b5262736d73696e3130326e44616b6a"
# [Code 3]
def getSeoulItem(start_num,end_num):
    base = "http://openapi.seoul.go.kr:8088/"

    parameter = f'{Itemkey}/json/ChunmanFreeSuggestions'
    parameter += f'/{start_num}'
    parameter += f'/{end_num}'

    url = base + parameter
    print(f'>>> URL : {url}')

    responseDecode = getRequestUrl(url)
    if responseDecode == None :
        return None
    else :
        return json.loads(responseDecode)

#[Code 2]
def getRequestUrl(url) :
    req = urllib.request.Request(url)
    try :
        response = urllib.request.Request(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e :
        return None

# [Code 1]
def main() :

    start_num = input("첫번째 페이지 번호 : ")
    end_num = input("마지막 페이지 번호 : ")

    jsonResult = []
    jsonResult = getSeoulService(start_num,end_num)
    print(jsonResult)

    with open(f"ChunmanFreeSuggestion__{start_num}__{end_num}.json","w",encoding="utf-8") as file :
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)

if __name__ == "__main__" :
    main()