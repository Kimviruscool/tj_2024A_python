# 1_파일읽기쓰기.py

#(1)파일 생성하기, open(파일이름 , 열기모드)
    #열기모드 : r읽기 , w쓰기 , a추가
    #파일열기 : 파일객체변수 = open(파일이름, 열기모드)
    #파일닫기 : 파일객체변수.close()

#1. 파일 열기
f = open('새파일.txt' , 'w') #쓰기 모드의 파일객체를 반환 함수.
print(f) 
#2. 파일 닫기
f.close()

#(2) 파일을 쓰기 모드로 열어 내용 쓰기, 파일객체변수.write(내용물)
f = open("C:/doit/새파일.txt" , 'w') #해당경로의파일을 쓰기모드로 열기
#실제 폴더가 존재해야한다
#write
for i in range(1, 11) : #1 ~10 까지 반복
    #들여쓰기 주의
    data = f'{i}번째 줄입니다.\n'
    #파일의 내용쓰기
    f.write(data) #
f.close()

#(3) 파일을 읽는 여러가지 방법
#1. readline(), 파일의 첫번째 줄을 읽어오는 함수
f= open("C:/doit/새파일.txt" , 'r') #해당 경로의 파일을 읽기 모드로 열어서 객체 반환
line = f.readline() #1번째 줄입니다.
print(line)
while True :
    line = f.readline()
    if not line :
        break
    print(line)
#2. readlines
f = open("C:/doit/새파일.txt" , 'r')
lines = f.readlines()
print(lines) #파일전체를 객체로 읽어온다
for line in lines : 
    print(line)
f.close()
#3. .read
f = open("C:/doit/새파일.txt" , 'r')
data = f.read() #파일내 내용 전체를 문자열로 읽어온다.
print(data)
f.close() #파일닫기

#4. 파일 객체와 for문 , 파일 객체는 기본적으로 for문과 함께 사용하여 줄 단위로 읽을 수 있다.
f = open("C:/doit/새파일.txt" , 'r')
for str in f: #파일객체내 한줄씩 반복변수에 대입하여 반복처리 한다.
    print(str)
f.close()

#(4) 파일에 새로운 내용 추가
f = open("C:/doit/새파일.txt" , 'a') #추가모드로 파일 객체 반환
for value in range(11, 20) :
    data = f'{value}번째 줄입니다\n'
    f.write(data) #파일에 내용쓰기
f.close() #파일 닫기

#(5) with, with 자료 as 변수 : with절 에서 자원을 획득하고 사용하고 반납 한다.
#파일은 항상 파일을 열고 작업이 끝나면 파일 닫기 해야했다.
    #with 자료 as  변수 :
        #해당 자료를 변수에 대입하고 with 가 종료되면 자동으로 변수는 초기화
with open('foo.txt', 'w') as f :
    #open 된 파일을 f변수에 대입하고 with작업이 종료되면 f변수도 초기화, close된다.
    f.write("Life is too short, you need python")
#day 04폴더에 foo.txt파일 생겼는지 , 내용 확인하기