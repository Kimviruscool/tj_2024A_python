# 6_if.py
from pyexpat.errors import messages

#
money = True #변수
if money :
    print("택시를 타고 가라")
else:
    print("걸어가라")
# moeny변수의 값이 True 이므로 '택시를 타고 가라' 출력

#(1) if의 기본구조
'''
if 조건문 :
(들여쓰기)수행문;
else :
(들여쓰기)수행문;
'''

#(2) 들여쓰기 방법
    #1. if문에 속하는 모든 실행문은 들여쓰기를 해야한다.
    #2. 주의할점 : 다른 프로그래밍 언어를 사용해온 사람들은 간과 하므로 무시 하므로 주의하자.
    #3. tab(탭)키 , 파이참/인텔리제이 에서 코드 범위 지정후 ctrl,alt,L

if money :
    print('택시를')
print('타고')
#     # print('가라') #IndentationError: unexpected indent

if money :
    print('택시를')
    print('타고')
        # print('가라') #IndentationError: expected an indented

#(3) 조건문 이란 무엇 인가?
    # - 조건문 이란 참 과 거짓을 판단 하는 문장
#1. 비교 연산자 : > 초과, < 미만, >= 이상, <= 미만, ==같다, != 같지 않다
x = 3
y = 2
print(x > y) #True
print(x < y) #False
print(x == y) #False
print(x != y) #True
print(x >= y) #True
print(x <= y) #False
#예제 1
# #money(2000) >= 3000, False
money = 2000
if money >= 3000 :
    print('택시를 타고 가라')
else :
    print('걸어 가라')
    # 결과 : 걸어 가라

#2. 논리 연산자 : and 이면서 , or 이거나 , not 아니면(부정)
#moeny(2000) or card >= 3000 , True
money = 2000
card = True
if money >= 3000 or card :
    print('택시를 타고 가라')
else :
    print('걸어 가라')
    #결과 : 택시를 타고 가라

#3. 기타 연산자 : in & not in
print(2 in [1,2,3]) #True #2가 [1,2,3] 에 포함 되는가?
print(2 not in [1,2,3]) #False #2가 [1,2,3] 에 포함 되지 않는가?
print('a' in ('a','b','c')) #True #a 가 (a,b,c) 에 포함이 되는가?
print('j' not in 'python') #True #j 가 python 에 포함 되지 않는가?

pocket = ['paper','cellphone','money']
if 'money' in pocket : #만약에 list(pocket) 안에 객체(money) 가 존재하면
    print('택시를 타고 가라')
    pass #pass 이후의 실행문은 실행되지 않는다.
else : #그게 아니면
    print('걸어 가라')
    #결과 : 택시를 타고 가라

#(4) 다양한 조건을 판단하는 elif (else if)
pocket = ['paper','cellphone']
card = True
if 'money' in pocket : #만약 pocket 에 money가 존재 하면
    print("택시를 타고 가라")
elif card : #money는 없고 card 가 존재 하면
    print("택시를 타고 가라")
else : #그게 아니면
    print("걸어 가라")
    #결과 : 택시를 타고 가라

#(5) 조건부 표현식 , if대신에 간단한 조건문 표현
    #참인경우 if 조건문 else 거짓일경우
score = 80
messages = "success" if score >60 else "failure" 
#messages = 기본값 if(만약) 점수가 60 초과이면 아니면 "실패" 출력
print(messages) # 결과 : success