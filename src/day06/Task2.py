# day06 > Task2.py
# 리스트 활용
from operator import index

#전역 변수
names = ['유재석','강호동','kim'] #샘플 작성 *데이터 다루는 방법 생각하기

    # 하나의 변수에 여러개의 이름을 저장하는 방법
    # 변수란? 하나의 자료를 저장하는 메모리 공간
    # 하나의 자료에 여러가지 속성을 담는 방법
        # 1. 객체 , 2. 문자열(JSON형식 , csv형식 ) 3. 리스트 4. 튜플
        #타입(자료 분류) vs 형식 (자료 모양)
        # "10" : 문자열 vs 숫자형식
        #  10 : 정수타입 vs 숫자형식
        # "{key : value}" : 문자열타입 vs JSON형식
        #  {key : value}  : JSON/딕셔너리 타입 vs JSON/딕셔너리 형식
    # CSV 란? : 몇 가지 필드를 쉼표(,)로 구분한 텍스트
    
#함수 정의, def 함수명(매개변수, 매개변수) :
def nameCreate():
    global names #전역변수 호출
    addName = input('addName : ')
    names.append(addName)
    return

def nameRead():
    global names
    for name in names :
        print(f'name : {name}')
    return

def nameUpdate() :
    global names #전역변수 호출
    oldName = input("oldName : ")

    if names.count(oldName) == 0 : return
    else:
        index = names.index(oldName)
        newName = input("newName : ")
        names[index] = newName

    return

def nameDelete() :
    global names
    oldName = input("oldName : ")

    if names.count(oldName) :
        names.remove(oldName)
    return


while True : #무한루프
    ch = int( input("1.Create 2.Read 3.Update 4.Delete : ") )
    if ch == 1 : nameCreate()

    elif ch == 2 : nameRead()

    elif ch == 3 : nameUpdate()

    elif ch == 4 : nameDelete()