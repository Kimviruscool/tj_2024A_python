# 1_class.py
#클래스란 ? 객체를 실체화 하기위한 설계도 , 빠른 생성 가능
#인스턴스 ? 객체가 실체화된 메모리
#객체 ? 물리적/추상적 으로 고유성질(변수) 과 행위(함수)를 정의한것

#[1] 클래스 구조 만들기
#(1) 간단한 클래스
class Fourcal :
    pass #아무것도 수행하지 않는 문법으로, 임시로 코드를 작성할 때 주로 사용된다. -Python

a = Fourcal() #객체생성
print( type(a) ) #type() 타입 반환해주는/확인하는 함수
# 결과 - 타입출력
# <class '__main__.Fourcal'>


#[2] 클래스내 메소드(함수) 만들기
#(1) 클래스내 메소드  선언
class Fourcal : # 클래스생성

    # 생성자
    #다중 생성자 불가능 / 단일 생성자
    def __init__(self,first,second) :
        self.first = first
        self.second = second

    #함수는 메소드/static 영역 # 함수 코드는 객체들이 공유 사용
    def setdata(self,first,second): #메소드(함수) 생성
        #매개변수란 ? : 함수 호출 시 전달되는 인자 값을 저장하는 변수
        #self : 자신,객체
        self.first = first #필드 값 초기화
        self.second = second #필드 값 초기화
        #함수를 호출한 객체(self)내 second 변수를 선언하고 매개변수(2)를 저장한다.

    #덧셈 함수 생성 
    def add(self):
        result = self.first + self.second #result 지역변수 / 함수 내 에서만 사용되고 함수종료시 초기화
        return result #return 함수 종료시 함수를 호출한 곳으로 반환되는 값
    #곱셈 함수 생성
    def mul(self):
        result =self.first * self.second
        return result
    #뺄셈 함수 생성
    def sub(self):
        result = self.first - self.second
        return result
    #나눗셈 함수 생성
    def div(self):
        result = self.first / self.second
        return result
    
#(2) 객체 생성
# a = Fourcal()
# #(3) 객체내 메소드 실행
# a.setdata(4,2)
# #(4) 객체내 필드 값 호출
# print(a.first)
# print(a.second)
#
# print(a.add()) #6
# print(a.mul()) #8
# print(a.sub()) #2
# print(a.div()) #2.0
#
# b = Fourcal() #객체 생성 , a에 저장된 객체와 b에 저장된 객체는 다르다.
# b.setdata(3,7)
# print(b.first)
# print(b.second)

c = Fourcal(4,8) #객체 생성 생성자 매개변수
print(c.first)
print(c.second)

#[4] 상속
#(1) 하위 클래스 정의 , class 클래스명(상위클래스명) : 
class MoreFourCal(Fourcal) : #extends
    def pow(self):
        return self.first ** self.second
    #오버라이딩 : 상위클래스의 메서드 재정의
    def div(self): #메서드 선언부를 동일하게 작성
        if self.second == 0 :
            return
        else:
            return self.first / self.second


#(2) 하위 클래스로 객체 생성
a = MoreFourCal(4,2)
print(type(a)) #<class '__main__.Fourcal'>

print(a.add()) #상위 클래스 메소드 호출

print(a.pow()) #본인 클래스 메소드 호출

print(a.div()) #오버라이딩 된 메소드 호출

#[5] 클래스 변수
#객체 변수 : 객체 마다의 변수 #객체변수명.변수명 #필드 , 멤버변수 라고도 한다.
#클래스 변수 : 모든 객체가 공유 해서 사용하는 변수 #클래스명.변수명 #static
#객체변수와 클래스변수의 이름이 같아도 식별이 가능하다.
class Family :
    lastname = "김" #클래스변수

print(Family.lastname) # 김
a = Family()
b = Family()
print(a.lastname) #김
print(b.lastname) #김
Family.lastname = "박"
print(a.lastname , b.lastname) #박 박