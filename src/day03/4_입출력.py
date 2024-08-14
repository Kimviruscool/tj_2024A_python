# 4_입출력.py

#(1) 사용자 입력, input() 함수
    #input('안내문구')
    #콘솔에 입력받은 값을 문자열(str)로 반환 해주는 함수
    #타입 확인 함수 : type(자료)
    
a = input() # JS prompt() Java Scanner
#Life is too short, you need python 입력
print(a)

number = input('숫자를 입력 하세요\n')
print(number)
print(type(number)) # type = 'str'

#(2) print 자세히 보기 , print() 함수
    #print(리터럴 또는 변수명 또는 연산식 )
    #print(f'문자열 { 변수명 또는 리터럴 또는 연산식 } 문자열') : f포메팅
    #print(리터럴 또는 변수명 또는 연산식 , end="출력 후 대입할 문자열") : 기본값 \n
print(123) # 숫자 출력
print("Python") # 문자열 출력
print([1,2,3,4]) #리스트 출력

print("python" + " is not bad") # +연산자를 이용한 문자열 연결
print("python","is fun") # , 쉼표 이용한 문자열 연결
# 출력후 결과값을 변경 하기 , 줄바꿈 대신에 다른 문자열 넣을 수 있다.
print('python' , end=' ') # end='\n' 기본값 이지만 변경이 가능하다.
print('is fun')