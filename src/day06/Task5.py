# day06 > Task5.py
# 딕셔너리/리스트 활용 , 파일처리 , p.175 ~ p.182

# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기

# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 여러명의 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.

# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.

# [조건4] : 프로그램이 종료되고 다시 실행되더라도 기존의 names 데이터가 유지 되도록 파일처리 하시오.
#           - dataLoad() , dataSave() 함수를 정의하여 적절한 위치 에서 호출 하시오.

# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출
# 파일내 데이터 설계 : 다수의 이름과 나이가 있을 때 저장하는 방법 샘플 설계
    #CSV : 필드 구분 , 객체 구분 \n


names = [] #샘플 데이터

def dataLoad(): #읽기 r , 프로그램 시작 시, while True 위에
    global names
    f = open('names.txt', 'r') #파일 읽기모드 로 객체 반환
    var = f.read()                  #파일내 데이터 전체읽어보기 #파일객체.read()
    #파일내 문자열 > 딕셔너리 만들고 리스트에 담기
    lines = var.split('\n') #줄마다(요소)
    #딕셔너리 생성 리스트에 담기
    for line in lines[ : len(lines)-1 ]: #읽어온 파일 내용 \n 분해 # \n 으로 객체 구분중 #마지막줄 제외
        dic = {'name' : line.split(',')[0], 'age' : line.split(',')[1] } #해당 줄에 ,(쉼표) 분해 [0] 이름 [1] 나이
        names.append(dic)
    f.close()
    print(names)
    return
#//////////////////////////////////////////////////////////////////////////
def dataSave() : #저장/쓰기 w , create , update ,delete
    global names
    #1. 파일에 데이터 쓰기
    f = open('names.txt','w')
    #딕셔너리 > 문자열 만들고 파일 쓰기
    outstr = "" #파일에 작성할 문자열 변수
    for dic in names :
        outstr += f'{dic['name'],dic['age']}\n' #딕셔너리를 CSV형식의 문자열로 변환 #,(쉼표) 필드 구분 #\n(줄바꿈) 객체/딕셔너리 구분

    f.write(outstr)
    f.close()
    return
#//////////////////////////////////////////////////////////////////////////
#함수 정의, def 함수명(매개변수, 매개변수) :
def nameCreate():
    global names #전역변수 호출
    addName = input("addName : ")
    addAge = input("addAge : ")
    addUser = {'name' : addName, 'age' : addAge}
    names.append(addUser)

    dataSave()
    return

def nameRead():
    global names
    for dic in names :
        print(f'name : {dic['name']} age : {dic['age']}')
    return

def nameUpdate() :
    global names #전역변수 호출
    oldName = input("oldName : ")
    for dic in names :
        if dic['name'] == oldName :
            newName = input("newName : ")
            newAge = input("newAge : ")
            dic['name'] = newName
            dic['age'] = newAge
            dataSave()
            return

    dataSave()
    return

def nameDelete() :
    global names
    delName = input("DeleteName : ")
    for dic in names :
        if dic['name'] == delName :
            names.remove(dic)
            dataSave()
            return

    return

dataLoad() #프로그램실행시 파일내용 읽어오기
while True : #무한루프
    ch = int( input("1.Create 2.Read 3.Update 4.Delete : ") )
    if ch == 1 : nameCreate()

    elif ch == 2 : nameRead()

    elif ch == 3 : nameUpdate()

    elif ch == 4 : nameDelete()