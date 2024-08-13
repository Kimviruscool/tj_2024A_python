#1.튜플.py
# - 리스트와 거의 비슷
# - 차이점 : 리스트 [] 수정 가능 , 튜플() 수정 불가능
t1 = ()
t2 = (1,) #단지 1개의 요소를 가질 때는 요소 뒤에 쉼표를 붙인다.
t3 = (1,2,3)
t4 = 1,2,3 # ( ) 소괄호 생략 가능
t5 = ('a','b',('ab','cd'))

#(2) 튜플의 요소 삭제 및 값 변경
t1 = (1,2,'a','b')
# del t1[0] #TypeError: 'tuple' object doesn't support item deletion : DELETE 요소를 지원하지 않는다.
# t1[0] = 'c' #TypeError: 'tuple' object doesn't support item assignment : 할당 할수 없다.

#(3) 튜플 다루기
# 1. 인덱싱 가능하다.
print(t1[0]) #1
print(t1[3]) #b
# 2. 슬라이싱 가능하다.
print(t1[1:]) #(2,'a','b')
# 3. 튜플의 연산
t2 = (3,4)
t3 = t1+t2
print(t3) #((1, 2, 'a', 'b'), (3, 4))

t3 = t2 * 3 #(3,4) * 3 = 3번 반복 추가
print(t3) #(3, 4, 3, 4, 3, 4)

#(4) 튜플의 길이
print(len(t1)) #4 튜플의 길이(개수) 구하기
