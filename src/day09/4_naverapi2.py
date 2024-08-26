# 4_naverapi2.py
import urllib.request
import json


#연습문제 : 2_naverapi.py 참고하여 네이버api로 블로그에서 입력받은 값 에 대한 검색 결과를 크롤링하여 JSON 파일로 저장하시오.

#[Code 4]
def getPostData(post,jsonResult,cnt) :

    title = post['title']
    description = post['description']
    # org_link = post['originallink']
    link = post['link']
    bloglink = post['bloggerlink']
    blogname = post['bloggername']


    dic = {'cnt' : cnt , 'title' : title , 'description' : description, 'bloglink' : bloglink , 'link' : link, 'blogname':blogname}
    jsonResult.append(dic)

#[Code 3]
def getNaverSearch(node,srcText,page_start,display) :
    base = "https://openapi.naver.com/v1/search"
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&start={page_start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None : return None
    else : return json.loads(responseDecode)

NaverID = "ZL2mvZCaGouQidwZFgBJ"
NaverPW = "Sst5w27S09"
#[Code 2]
def getRequestUrl(url) :
    req = urllib.request.Request(url)
    req.add_header("X-naver-Client-Id", NaverID)
    req.add_header("X-naver-Client-Secret", NaverPW)

    try: #예외처리
        responses = urllib.request.urlopen(req) #지정한 url 실행후 응답 반환
        print(f'>>>code2 요청URL 결과 상태 : {responses.getcode()}') #확인
        if responses.getcode() == 200:  #만약에 응답의 상태가 200(성공) 이면
            return responses.read().decode('utf-8') #실행된 url내 모든 내용물 읽어 오기
    except Exception as e :
        return None #없으면 None
#[Code 1]
def main():
    node = 'blog'
    srcText = input('검색어 입력하세요 : ')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node,srcText,1,100)

    total = jsonResponse['total']

    while((jsonResponse != None) and (jsonResponse['display'] != 0 )) :
        for post in jsonResponse['items'] :
            cnt += 1
            getPostData(post,jsonResult,cnt)

        start = jsonResponse['start'] + jsonResponse['display']

        jsonResponse = getNaverSearch(node,srcText,start,100)
        
    print(f'전체 검색 : {total}건 ')
    print(f'가져온 데이터 : {cnt}건')

    with open(f'{srcText}-naver-{node}.json','w',encoding='utf-8') as file :
        jsonFile = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        file.write(jsonFile)

if __name__ == "__main__" :
    main()