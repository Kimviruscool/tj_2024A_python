# DAY09 > 1_URL.py
#urllib : URL 작업을 위한 여러 모듈을 모은 패키지


#[1] urllib.requestt : URL 요청에 관련 기능을 제공하는 라이브러리
    #1. urllib.request.Request(URL) : 지정한 URL에 대한 요청 객체를 반환
    #2. urllib.request.urlopen(요청객체) : 지정한 요청 객체를 실행하고 응답 객체를 반환
    #2-1. 응답객체.getcode() : 응답 상태 반환 (200 : 성공 , 400 : 실패(요청문제) , 500: 실패(백엔드 문제) )
    #2-2. 응답객체.read() : 응답 내용 모두 읽어오기 
    #2-3. 응답객체.read.decode('utf-8') : HTML형식과 한글 형식을 지원해준다. read는 한번만 가능
    #3. urllib.parse.quote(문자열) : 지정한 문자열을 HTTP 바이트로 변환

import urllib.request #1. request 모듈 호출
url = "https://www.example.com" #2. 요청을 보낼 url 주소를 가지는 변수
request = urllib.request.Request(url) #3. Request 객체 생성 #지정한 URL에 대한 요청을 생성
response = urllib.request.urlopen(request) #4. url메소드를 이용한 url에 대한 요청을 실행하고 응답을 반환 함수
print(response) # <http.client.HTTPResponse object at 0x0000019EF36FF460>
print(response.getcode()) #200
print(response.read()) #b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
print(response.read().decode('utf-8')) #결과
#<!doctype html>
# <html>
# <head>
#     <title>Example Domain</title>
#
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#
#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         div {
#             margin: 0 auto;
#             width: auto;
#         }
#     }
#     </style>
# </head>
#
# <body>
# <div>
#     <h1>Example Domain</h1>
#     <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
#     <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>