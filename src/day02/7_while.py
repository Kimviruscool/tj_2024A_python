# 7_while.py
# - 문장을 반복해서 수행해야 할 경우

#(1) while문의 기본 구조
'''
1. java
while(true){
    실행문;
    조건문;
}

2. python
while 조건문 :
    실행문;
'''
treeHit = 0 #변수
while treeHit < 10: #변수가 10 미만 이면 반복 하고 아니면 [반복]을 종료 한다는 뜻
    treeHit = treeHit + 1 #반복하며 treeHit 에 +1
    print(f'나무를 {treeHit}번 찍었습니다.') # F포메팅 : f'문자열 {변수,연산식} 문자열' #java ` `(백틱)유사
    if treeHit == 10 : #만약 treeHit 가 10과 같으면
        print("나무 넘어갑니다.") #출력 후 함수 정지
#while , if사용할때 주의할 점 : {}(중괄호) 가 없고 들여쓰기를 이용한 실행문을 작성해야함

#(2) while문 만들기
number = 0
while number != 4 :
    print("1.ADD 2.DEL 3.List 4.Quit \nEnter Number : ")
    number = int(input()) 
    #input() : 콘솔창에서 입력받은 값을 반환 해주는 함수
    #int() : 자료를 정수타입으로 반환해주는 함수
    #while , if 에서는 : 들여쓰기 주의

#(3) break 키워드 : 가장 가까운 *[반복문] 종료 vs return *[함수] 종료
coffee = 1 #변수
while True : #무한루프 
    # * [ : 콜론 나올때 마다 들여 쓰기 주의 ]
    money = int(input("돈을 넣어 주세요 : ")) #input(입력전 출력 문구) #int(자료) : 해당 자료를 정수 타입 반환 함수 vs JAVA : Inteeger.parseInt() vs JS: parseInt()
    if money == 300 : # 만약에 입력받은 값이 300 이면
        print("커피를 줍니다.")
        coffee = coffee -1 #coffee -1
        print(f"현재 커피가 {coffee}개 남았습니다")
    elif money > 300 : # 아니면 vs java/js : else if
        print(f"거스름돈 {money-300}를 주고 커피를 줍니다.") # f 포메팅 : f'문자열{코드}'문자열'
        coffee = coffee -1 # coffee - 1
        print(f"현재 커피가 {coffee}개 남았습니다.")
    else : #아니면
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.") # f 포메팅 : f'문자열{코드}문자열'

    if coffee == 0 : #만약에 (if) coffee 가 0개이면 
        print(f"커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break #break 실행 (가장 가까운 반복문 종료)

#(4) continue 키워드 : 가장 가까운 반복문 으로 강제 이동
a = 0 # 초기값 설정
while a < 10 : # 반복 조건문
    a = a + 1 # a의 값을 1증가 , 증감식
    if a % 2 == 0 : continue # a의 값이 짝수 이면 : (continue) 가장 가까운 반복문 으로 강제 이동 (아래 코드는 실행되지 않는다.)
    print(a) # 짝수는 출력 되지 않고, 홀수만 출력

#(5) 무한 루프 : 조건이 항상 True 이므로 while 안에 있는 실행문은 무한 수행하게 된다.
while True :
    print("ctrl + C 를 누르면 종료됩니다. ")