# 1_class.py / p.190

'''
객체란 ?   논리적/물리적 정의한 실체물 (세상의 모든걸 코드화 할수있는것)
클래스란 ?  객체를 물리적으로 표현하기 위한 설계도 
인스턴스란? 클래스를 이용해서 객체를 물리적으로 만든 실체물 (코드화한 것 / 메모리를 할당한 것)

- java 클래스
class Calculator{
    int result; //필드
    Calculator(){}  //생성자
    int add(int num) {  //메소드
        this.result += num 
        return this.result
    }
}

- java 객체
Calculator cal1 = new Calculator();
Calculator cal2 = new Calculator();

- java 객체가 메소드 호출

cal1.add(3)
cal2.add(4)

'''

#[1] 파이썬 클래스 만들기 / class 클래스명 :
class Calculator :
    def __init__(self): #생성자
        self.result = 0

    def add(self,num):  #메소드
        self.result += num
        return self.result
#[2] 파이썬 객체 만들기 / 변수명 = 클래스명()
cal1 = Calculator()
cal2 = Calculator()

#[2-1] 주소값 확인
print(cal1) #<__main__.Calculator object at 0x0000017E5C9FD6D0>
print(cal2) #<__main__.Calculator object at 0x0000017E5C9FD700>

#[3] 파이썬 객체내 메소드 호출
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#[4] 클래스의 생성자 정의
#(1) 과자 클래스 정의
class 과자틀 :
    #파이썬은 기본적으로 다중 생성자를 지원하지 않는다. # 단일 생성자 , __init__ 메소드는 1개
    # def __int__(self):
    #     self.과자재료1 = None #None 이란? 데이터가 없다는 뜻
    #     self.과자재료2 = None
        
    #생성자1 : 매개변수 2개 갖는 생성자
    def __init__(self,재료1,재료2): #__init__ 생성자 역할을 하는 메소드
        #self : 해당 메소드를 실행하는 객체 (.this)
        self.과자재료1 = 재료1 #self.필드명 = 매개변수 #매개변수로 필드 값 초기화 하기
        self.과자재료2 = 재료2 #self.필드명 = 매개변수 #매개변수로 필드 값 초기화 하기

#(2) 과자 객체 생성        
var1 = 과자틀('밀가루','초코')
var2 = 과자틀('밀가루','치즈')

#(2-1) 과자 주소 값
print(var1) #<__main__.과자틀 object at 0x000001535456E030>
print(var2) #<__main__.과자틀 object at 0x000001535456E090>

#(3) 객체의 필드 호출, 객체변수명.필드명
print(var1.과자재료1) #첫번째 객체/과자의 과자재료1 필드 값 호출 #밀가루
print(var1.과자재료2) #첫번째 객체/과자의 과자재료2 필드 값 호출 #초코
print(var2.과자재료1) #두번째 객체/과자의 과자재료1 필드 값 호출 #밀가루
print(var2.과자재료2) #두번째 객체/과자의 과자재료2 필드 값 호출 #치즈

#(4) 객체의 필드 값 수정 : 객체변수명.필드명 = 새로운 값
# var3 = 과자틀(); print(var3)
#TypeError: 과자틀.__init__() missing 2 required positional arguments: '재료1' and '재료2'
# 파이썬은 기본적으로 다중 생성자를 지원하지 않는다. # 단일 생성자

var2.과자재료2 = '녹차'
print(var2.과자재료2) #녹차 로 변경
