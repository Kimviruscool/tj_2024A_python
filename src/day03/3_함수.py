# 3_함수.py
# - 입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어 놓는 것
# - 사용목적 : 1.코드재활용(반복사용) 2.기능분리

#(1) 파이썬의 함수의 구조
'''
(1) py
def 함수명(매개변수, 매개변수) : 
    실행문
    return 반환값

(2) JS
function 함수명 (매개변수 , 매개변수){
    실행문
    return 반환값 또는 생략
}

(3) JAVA
public 반환타입(void,int) 함수명(타입 매개변수 , 타입 매개변수){
    실행문;
    return 반환값 또는 생략
}

'''

#예1 : 함수의 이름은 add 이고 입력으로 2개(a,b)은 2개의 입력값을 더한 값이다.
def add(a,b) :
    #{ } 가 없으므로 들여쓰기 주의
    return a + b
#함수 호출
add(3,4)
print(add(3,4)) #7
a = 3
b = 4
result = add(a,b) #리터럴 대신 변수를 대입해도 된다.
print(result) #7

#(2) 입력값 과 리턴값 의 따른 함수의 형태

#1. 매개변수 O 리턴 o
def add(a,b) : #함수 정의
    result = a+ b
    return result
a = add(3,4) #함수 호출 시 인수2개 전달하여 반환값을 받아 'a'변수에 저장
print(a)

#2. 매개변수 X 리턴 o
def say() : #함수 정의
    return 'HI'
a = say() #함수 호출 시 인수 전달이 없고 반환값을 받아 'a'변수에 저장
print(a)

#3. 매개변수 o 리턴 x
def add(a,b) : #함수 정의
    print(f'{a},{b}의 합은 {a+b}입니다.')
add(3,4) #함수 호출 시 인수 2개 전달하여 반환값은 없다

#4. 매개변수 x 리턴 x
def say() : #함수 정의
    print('HI')
say() #함수 호출 시 인수 없고 반환값도 없다.

#(3) 매개변수를 지정하여 호출 하기
def sub(a,b) :
    return a - b
result = sub(b=3 , a=7)
print(result)

#(4) 입력값이 몇 개가 될지 모를 때 , 가변 매개변수
# 1. *매개변수 : 매개변수 이름앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어준다.
#함수 정의, * 
def add_many(*args) :
    print(args) #여러개의 매개변수 값이 들어있는 리스트 !튜플 타입
    result = 0 #더한 값을 저장하기 위한 변수
    for i in args :
        result += i
        #for 종료후
    return result # 함수 종료시 반환되는값
#함수 호출
result = add_many(1,2,3); print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10); print(result)

#예제2.
def add_mul(choice, *args):
    print(choice) # 1개의 자료 매개변수
    print(args) # 여러개의 자료를 가지는 튜플(매개변수)
    if choice == "add": #만약에 매개변수 값이 add 이면
        result = 0
        for i in args:
            result += 1
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul',1,2,3,4,5)
print(result)

#(5) 키워드 매개변수 .kwargs ,** 인수로 전달된 키와값을 딕셔너리의 매개변수로 받는다.
def print_kwargs(**kwargs):
    print(kwargs) # {'a': 1} : 딕셔너리 타입으로 매개변수를 받는다.
print_kwargs(a = 1) # 인수로 전달시 키 와 값으로 전달
print_kwargs(name="foo", age = 3) #{'name': 'foo', 'age': 3}

#(6) 함수의 리턴값은 언제나 하나이다, 여러개 = [],(),{} 활용
#1.
def add_and_nul(a,b):
    튜플 = 1, 2 #1,2
    print(튜플)
    return a+b , a*b
#함수 호출
result = add_and_nul(3,4) #7,12
print(result)

#2. 동일한 수준의 return는 하나만 존재 해도 된다.
def add_and_nul(a,b):
    return a+b
#   return a*b #위에 리턴이 존재하므로 해당 리턴은 실행되지 않는다.

#3. 서로 다른 수준의 return은 여러개 존재 할 수 있다.
def add_and_nul(a,b):
    if a<0:
        return  #만약에 a가 0보다 작으면 함수 강제 종료 , 아래코드는 실행되지 않는다.
    return a +b

#(7) 매개변수에 초깃값 미리 설정하기
    #주의할점 : 초기화 하고 싶은 매개변수는 항솽 뒤쪽에 놓아야한다.
    #say_myself(name,age,man = True) [O]
    #say_myself(name,man = True,age) [X]
def say_myself(name,age,man = True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
#함수 호출
    # 만약에 해당 매개변수의 인자값이 없으면 디폴트 값이 대입된다.
say_myself('박응용',27) #나의 이름은 박응용입니다. 나이는 27살입니다. 남자입니다.
say_myself('박응용',27,False) #나의 이름은 박응용입니다. 나이는 27살입니다. 여자입니다.

#(8) 함수 안에서 선언한 변수의 효력 범위, 지역변수
    # 함수 안에서 사용하는 매개변수는 함수 밖에 변수 이름과 전혀 무관 하다.
a = 1 # 전역변수 'a'
def vartest(a):
    a = a + 1 #지역변수 'a' , a = 2 지역 변수의 2는 함수 종료 시 사라진다.
vartest(a)
print(a) # 전역변수 'a'의 값 확인, 1

# 함수 안에서 함수 밖 변수를 함수안에서 활용하는 방법
#1. return , 권장 한다.
a = 1
def vartest(a) :
    a = a + 1
    return a #지역변수는 함수 종료시 사라지므로 함수를 호출했던 곳으로 반환
a = vartest(a)
print(a) #2
#2. global 키워드 : 함수 밖 변수를 함수 안으로 호출할때 사용하는 키워드
a = 1
def vartest():
    global a #함수 밖에 있는 a변수를 함수 안으로 호출
    a = a + 1
vartest()
print(a) #2

#3. 함수 밖에서 함수 안으로 접근 가능 하지만 , 함수 안에서 함수 밖 으로는  접근이 불가능
b = 1
def vartest() :
    c = b + 1 #함수 밖에 있는 b변수를 함수 안에서 호출, global 없이도 가능.
    return c
b = vartest()
print(b) #2