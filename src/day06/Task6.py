# day06 > Task6.py
# 객체/리스트 활용 190p. ~ 207p
# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기
# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 객체들을 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출

names = []

class User :
    def __init__(self,name,age):
        self.name = name #필드 값 초기화
        self.age = age #필드 값 초기화

# 함수 정의, def 함수명(매개변수, 매개변수) :
def nameCreate():
    global names  # 전역변수 호출
    addName = input("addName : ")
    addAge = input("addAge : ")

    names.append(User(addName, addAge))
    return


def nameRead():
    global names
    for dic in names :
        print(f'name : {dic.name} age : {dic.age}')
    return


def nameUpdate():
    global names  # 전역변수
    oldName = input("oldName : ")
    for dic in names :
        if dic.name == oldName :
            dic.name = input("newName : ")
            dic.age = input("newAge : ")
            return
    return


def nameDelete():
    global names
    delName = input("delName : ")
    for dic in names :
        if dic.name == delName :
            names.remove(dic)
            return
    return


while True:  # 무한루프
    ch = int(input("1.Create 2.Read 3.Update 4.Delete : "))
    if ch == 1:
        nameCreate()

    elif ch == 2:
        nameRead()

    elif ch == 3:
        nameUpdate()

    elif ch == 4:
        nameDelete()