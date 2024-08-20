# Task1.py
# 문자열 활용 p.50 ~ p.76
#[조건1] : 각 함수들의 구현해서 프로그램 완성

#[조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#         2. 저장된 여러명의 이름을 모두 출력
#         3. 수정할 이름 존재하면 새로운 이름을 입력받아 수정
#         4. 삭제할 이름을 입력받아 존재하면 삭제
#[조건3] : names외 추가적인 전역 변수 생성 불가능.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출

names = "" # 여러개 name들을 저장하는 문자열 변수

def nameCreate() :
    global names
    names += input("이름 입력 : ")
    names += " "
    return

def nameRead() :
    print(names)
    return

def nameUpdate() :
    name = input("존재하는 이름 입력 : ")
    if names.count(name) >= 1 :
        namae = input("바꿀 이름 입력 : ")
        return names.replace(name,namae) # *replace 불변
    else: print("존재하지 않는 이름")
    return

def nameDelete() :
    name = input("삭제할 이름 입력 : ")
    if names.count(name) >= 1 :
        delname = ""
        return names.replace(name,delname) # *replace 불변
    else: print("존재하지 않는 이름")
    return

while True : #무한루프
    ch = input("1.Create 2.Read 3.Update 4.Delete : ")
    if ch == "1" :
        nameCreate()
    elif ch == "2" :
        nameRead()
    elif ch == "3" :
        names = nameUpdate() #불변 이기 때문에 함수 밖에서 다시 return 값을 다시 대입 해야한다.
    elif ch == "4" :
        names = nameDelete() #불변 이기 때문에 함수 밖에서 다시 return 값을 다시 대입 해야한다.