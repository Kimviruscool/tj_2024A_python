# 1_크롤링.py

# 정적 웹 페이지 크롤링
'''
[1] 설치
from bs4 improt BeautifulSoup
[2] HTML 파싱
변수명 = BeautifulSoup(html파일객체,"html.parser")
변수명 = BeautifulSoup(html형식의문자열,"html.parser")
[3] 파싱 메소드, 속성
    1. .find(식별자 , 속성명 = 값) : 지정한 식별자 과 속성명 동일한 태그 조회
        find(div)
        find(div, class="box1")
        find(div, id="box2")

    2. .select_one() :
        select_one(div 또는 .box1 또는 #box2)
        
    3. .findAll() : 지정한 식별자와 일치한 여러개 추출해서 리스트로 반환
    
    4. .select() :
    
    -
    0. .태그명 : 헤당 태그들의 첫번째 태그<마크업> 을 추출
    1. .text : 마크업 사이의 문자열 반환, 자식,자손 모두가능 , 주로 중첩텍스트 일때
    2. .string : 마크업 사이의 문자열 반환 , 자식만 가능 , 자손 불가능 , 주로 단일텍스트 일때
    3. .attrs : 해당 마크업의 속성 목록/리스트 반환
'''

#[1] 설치
from bs4 import BeautifulSoup
#[2] HTML 파일 객체
htmlFile = open("1_웹페이지.html", encoding="utf-8")
#[3] BeautifulSoup 객체 생성
htmlObj = BeautifulSoup(htmlFile, "html.parser")
print(htmlObj)
#[4] .find(식별자) : 지정한 특정 마크업 조회하기 && select_one(식별자)
print(htmlObj.find('div')) #<div> [1] 여기를 크롤링 하세요. </div>
print(htmlObj.select_one('div')) #<div> [1] 여기를 크롤링 하세요. </div>
# [5] .findAll(식별자) : 지정한 특정 마크업 여러개 조회하기 && select(식별자) #list로 반환됨
print(htmlObj.findAll('div')) #[<div> [1] 여기를 크롤링 하세요. </div>, <div class="box1"> [2] 여기를 크롤링 하세요. </div>, <div id="box2"> [3] 여기를 크롤링 하세요. </div>]
print(htmlObj.select('div')) #[<div> [1] 여기를 크롤링 하세요. </div>, <div class="box1"> [2] 여기를 크롤링 하세요. </div>, <div id="box2"> [3] 여기를 크롤링 하세요. </div>]
#[6] .text : 호출된 마크업의 있는 내용 문자열 추출 && .string
print(htmlObj.find('div').text) #[1] 여기를 크롤링 하세요.
print(htmlObj.find('div').string) #[1] 여기를 크롤링 하세요.
#[7] 반복문과 같이 활용
for div in htmlObj.select('div') : #모든 div를 추출해서 리스트에 반환 한 다음 리스트 만큼 반복문 처리
    print(div.string) # div 하나씩 내용물 추출
#[8] class 식별자 이용한 조회
print(htmlObj.find('box1')) #None
print(htmlObj.find('.box1')) #None
print(htmlObj.find('div',class_='box1')) #<div class="box1"> [2] 여기를 크롤링 하세요. </div> # _ 주의
print(htmlObj.select_one('.box1')) #<div class="box1"> [2] 여기를 크롤링 하세요. </div>
#[9] id 식별자를 이용한 조회
print(htmlObj.find('div',id='box2')) #<div id="box2"> [3] 여기를 크롤링 하세요. </div>
print(htmlObj.select_one('#box2')) #<div id="box2"> [3] 여기를 크롤링 하세요. </div>

#연습
html = '''
    <h1 id="title">한빛출판네트워크</h1>
    <div class="top">
        <ul class="menu">
            <li><a href="http://wwww.hanbit.co.kr/member/login.html"class="login">로그인</a>
            </li>
        </ul>
        <ul class="brand">
            <li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li>
            <li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li>
        </ul>
    </div>'''

#[1] html 파싱 객체
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()) #prettify() : 지정한 내용을 HTML 문서 형태로 출력
#[2] 태그(마크업) 파싱하기
print(soup.h1) #1. 파싱객체.마크업명 #<h1 id="title">한빛출판네트워크</h1>
print(soup.div) # <div clas='top'> ~~ </div>
print(soup.ul) # <ul class="brand"> ~~ </ul>
print(soup.li) #<li> ~~ </li>
print(soup.a) #<a class="login" href="http://wwww.hanbit.co.kr/member/login.html"> ~~ </a> #한개만 가져옴
print(soup.findAll("ul")) #[<ul class="menu"> ~~ </ul> , <ul class="brand"> ~~ </ul>]
print(soup.findAll("li")) #[<li><a class="login" href="http://wwww.hanbit.co.kr/member/login.html"> ~ </li> , <li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li> , <li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li>]
print(soup.findAll("a")) #[<a class="login" href="http://wwww.hanbit.co.kr/member/login.html">로그인</a>, <a href="http://www.hanbit.co.kr/media/">한빛미디어</a>, <a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a>]
#.attrs : 지정한 마크업의 속성 목록을 딕셔너리 반환
print(soup.findAll('a')[0].attrs) #{'href': 'http://wwww.hanbit.co.kr/member/login.html', 'class': ['login']}
print(soup.findAll('a')[0]['href']) #http://wwww.hanbit.co.kr/member/login.html
print(soup.findAll('a')[0]['class']) #['login']
print(soup.find('ul',attrs={'class' : 'brand'})) # <ul class="brand"> ~ </ul> / # find(마크업, class='클래스명')
print(soup.find(id="title")) #<h1 id="title">한빛출판네트워크</h1> / # .select_one(#ID명)
li_List = soup.select('div>ul.brand>li') #[<li> ~~ </li> ]
for li in li_List :
    print(li.string)