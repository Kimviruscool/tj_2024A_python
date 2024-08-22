# day07 3_예외처리.py
#예외란? 프로그램 실행 도중에 발생하는 오류를 다른 실행문으로 처리해주는 역할
from ast import Index

list = [1,2,3]
       #0,1,2
# list[3] #예외발생 : 존재하지 않는 index 이므로 예외 발생

try :
    #예외가 발생 할것 같은 코드들
    list[3]
except :
    print('존재하지 않는 인덱스입니다.')
#[2] 예외 처리 방법2    
try :
    list[3]
except IndexError : #특정 예외를 명시 할때는 예외 클래스명
    print('존재하지 않는 인덱스')
#[3] 예외 처리 방법3
try :
    list[3]
except IndexError as e : #특정 예외 가 발생한 사유를 보고싶을때 as 예외변수명 작성
    print(e)

#[4] finally
try :
    list[3]
except IndexError as e:
    print(e)
finally:
    print('예외 여부와 상관없이 실행')

#[5] 다중 exception , 다중 except 중 1번 또는 0번 실행된다.
try:
    list[3]
    # print(4/0)
    int("a")
except ZeroDivisionError as e: print(e) #ZeroDivisionError 예외 발생시
except IndexError as e:print(e) #IndexError 예외 발생시
except Exception as e: print(e) # 그외 모든 예외가 발생했을때 실행 #다중 예외 에서는 마지막에 사용한다.
