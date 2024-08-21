# day06 > Task2.py
#  딕셔너리 활용
from operator import index

#전역 변수
#리스트 [ ] 안에 여러개 딕셔너리 { } 가 저장된 구조
names = [{'name':'kim'},{'name':'lee'}] #샘플 작성 *데이터 다루는 방법 생각하기

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
    addName = input("addName : ")
    addNames = {'name' : addName}
    names.append(addNames)
    return

def nameRead():
    global names
    for dic in names : #리스트내 딕셔너리 하나씩 호출
        print(f'name : {dic['name']}') # 딕셔너리변수명[key] or 딕셔너리변수명.get('key')
    return

def nameUpdate() :
    global names #전역변수 호출
    oldName = input("oldName : ")
    for dic in names :
        if dic['name'] == oldName :
            newName = input("newName : ")
            dic['name'] = newName # 해당 딕셔너리의 속성값 수정
            return
    return

def nameDelete() :
    global names
    delName = input("delName : ")
    for dic in names :
        #만약에 삭제할 이름과 같으면
        if dic['name'] == delName :
            names.remove(dic) #리스트변수명.remove()
            return # 1개만 삭제하기 위해선 삭제 후 return
    return


while True : #무한루프
    ch = int( input("1.Create 2.Read 3.Update 4.Delete : ") )
    if ch == 1 : nameCreate()

    elif ch == 2 : nameRead()

    elif ch == 3 : nameUpdate()

    elif ch == 4 : nameDelete()