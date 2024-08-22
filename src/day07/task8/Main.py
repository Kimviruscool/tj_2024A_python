#task8 > main.py

'''
user.py user 객체의 정보를 가지는 클래스 정의
file.py save() , load() 함수를 정의
[조건1] 이름과 나이를 입력받아 저장
[조건2] 프로그램이 종료되고 다시 실행 해도 names 데이터가 유지 되도록 파일처리

'''

from User import User
from File import *

names = []

def nameCreate():
    global names  # 전역변수 호출
    addName = input("addName : ")
    addAge = input("addAge : ")

    names.append(User(addName,addAge))
    dataSave(names)
    return


def nameRead():
    global names
    for list in names :
        print(f'name : {list.name} age : {list.age}')
    return


if __name__ == "__main__" :
    names = dataLoad() #프로그램 실행시 파일 내용 읽기
    while True:  # 무한루프
        ch = int(input("1.Create 2.Read : "))
        if ch == 1:
            nameCreate()

        elif ch == 2:
            nameRead()