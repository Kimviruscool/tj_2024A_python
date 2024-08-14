# 1_for문.py
# - while 문과 비슷한 반복문
# - for문은 한눈에 들어온다는 장점

#(1)  for문의 기본 구조
'''
for 변수 in 리스트(또는 튜플 또는 문자열) :
    실행문;
'''
# 예제
test_list = ['one','two','three']
# 'test_list' 이라는 변수가 [one,two,three] 를 참조
# JS : let test_list = [one,two,three]
for i in test_list :
    # : 콜론 다음 실행문 작성시 들여쓰기 주의 , { } 없다.
    print(i)
# 예제2
a = [(1,2),(3,4),(5,6)]
for (first, last) in a :
    #리스트 내 튜플을 하나씩 (요소1,요소2) 튜플 타입으로 반환해서 반복처리 한다.
    print(first + last)
# 예제 3
marks = [90,25,67,45,80]  #학생들의 점수리스트
number = 0 #학생 번호
for mark in marks : #들여쓰기 주의
    number = number + 1 #학생 번호 1증가
    if mark >= 60 : #mark 가 60점 이상이면
        print(f"{number}번 학생은 합격입니다.")
    else: #그게 아니면
        print(f"{number}번 학생은 불합격입니다.")
        #파이썬의 if조건문에 ()가 없다.

#(2) continue
number = 0
for mark in marks :
    number = number + 1
    if mark < 60 :
        continue #가장 가까운 for문으로 이동 , continue 를 만나게 되면 아래 코드는 실행되지 않는다.
    print(f"{number}번 학생 축하합니다. 합격입니다.")

#(3) range () : 숫자 리스트를 생성해서 반환 해주는 함수
# range(숫자) : 0부터 숫자 미만 까지 포함 하는 range 객체를 만들어준다.
# range(시작숫자,끝숫자) : 시작 숫자 부터 끝 숫자 미만 까지 포함하는 range 객체를 만들어 준다.
# range(시작숫자, 끝숫자, 증감단위) :시작 숫자 부터 끝 숫자 미만 까지 증감단위 만큼 증감하여 포함하는 range 객체를 만들어 준다.
a = range(10)
print(a) #0,1,2,3,4,5,6,7,8,9
a = range(1,11)
print(a) #1,2,3,4,5,6,7,7,8,9,10

#예제
for value in range(10) : # 0 ~ 9
    print(value, end=' ') #print(값 , end=' ') : 줄바꿈 처리를 하지 않는 출력문

print()

for value in range(1,11) : # 1 ~ 10
    print(value, end=' ')

print()

for value in range(1,11,2) : #1~10 까지 2씩 증가 , 1,3,5,7,9
    print(value, end=' ')

print()

#예제 2 1부터 10까지 누적합계를 구하시오
sum = 0
for i in range(1,11) :
    sum += i;
print(sum)
#1분 코딩
sum = 0
for i in range(1,101) :
    sum += i;
print(sum)
#예제3 구구단
for i in range(2,10) :
    for j in range(1,10) :
        print(i*j, end=' ')
    print()

#(4) 리스트 컴프리헨션 사용 ,
# [표현식 for 항목 in 반복가능객체 if 조건문]
# [연산식 for 반복변수 in 리스트 if 조건문]
#1
a = [1,2,3,4]
# result = [실행문 for 반복변수 in 리스트]
result = [num*3 for num in a]
#[]안에서 for문을 사용한다
#[실행문 for 반복변수 in 리스트명]
print(result)

# 2.
result = [i for i in a]
#반복되고 있는 i 값을 하나씩 리스트 요소로 대입하여 리스트를 생성 한다.
print(result)

# 3. 기존 리스트를 반복문을 활용하여 새로운 리스트 생성
print([i for i in a]) # JAVA/JS : 리스트.map()

#4.
result = [num for num in a if num%2 == 0]
print(result)
#5. 2개 이상
result = [x*y for x in range(2,10)
            for y in range(1,10)]
print(result)