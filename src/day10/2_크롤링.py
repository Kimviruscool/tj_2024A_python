# 2_크롤링.py

from bs4 import BeautifulSoup #모듈 가져오기
import urllib.request

# [실습1] https://quotes.toscrape.com/
url = "https://quotes.toscrape.com/" #크롤링할 url
response = urllib.request.urlopen(url) #지정한 url 요청 후 응답 받기
htmlData = response.read() #응답 받은 내용물 전체 읽어오기
# print(htmlData)
soup = BeautifulSoup(htmlData, "html.parser") #지정한 html문자열로 html 파싱 객체 생성
print(soup.prettify()) #확인

#특정 마크업/태그 파싱
quoteaDivs = soup.select('.quote')
# print(quoteaDivs)
for quote in quoteaDivs :
    #명언 문구 만 추출
    print(quote.select_one('.text').string)
    #각 명언 저자 추출
    print(quote.select_one('.author').string)
    #각 명언 태그 목록 추출
    for tag in quote.select('.tag') :
        print(tag.string, end='\t')

    print('\n\n')

# [실습2] https://v.daum.net/v/20240827074833139
url = "https://v.daum.net/v/20240827074833139"
response = urllib.request.urlopen(url)
htmlData = response.read()
# print(htmlData)
soup = BeautifulSoup(htmlData, "html.parser")
# print(soup.prettify())

#파싱
pt = soup.select('p')
# print(pt)
# 기사 제목
print(soup.select_one('.tit_view').string)
print('\n\n')

for p in pt :
    #본문 내용(사진 제외)
    print(p.text)

#[실습 3] https://search.naver.com/search.naver?query=%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8(부평구날씨)
url = "https://search.naver.com/search.naver?query="+urllib.parse.quote('부평구날씨')
response = urllib.request.urlopen(url)
htmlData = response.read()

soup = BeautifulSoup(htmlData, "html.parser")
#온도 추출
print(soup.select_one('.temperature_text').text)
#습도 추출
print(soup.select_one('.summary_list').select('.sort')[1].text)
