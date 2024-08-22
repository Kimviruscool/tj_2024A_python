# 5_내장함수.py

#파이썬 배포본에 함께 들어 있는 함수들 = 라이브러리
# import 하지 않아도 된다.

# 1. abs(숫자) : 절댓값 리턴함수
print(abs(3)) #3
print(abs(-3)) #3
print(abs(-1.2)) #1.2

# 2. all(리스트/튜플/문자열/딕셔너리/집합) : 모두 참이면 참
# / 0 이면 FALSE 1 ~ * 이면 TRUE, [] 빈값 TRUE
print(all([1,2,3])) #True
print(all([1,2,3,0])) #False
print(all([])) #True
#2-7 bool연산자 참고

# 3. any(리스트/튜플/문자열/딕셔너리/집합) : 하나라도 참이면 참
# 값이 있으면 TRUE / 없으면 FALSE
print(any([1,2,3])) #True
print(any([1,2,3,0])) #True
print(any([])) #False

# 4. chr(유니코드) : 유니코드 숫자 값을 받아 문자로 반환
print(chr(97)) #a
print(chr(44032)) #가

# 5. dir(객체) : 객체가 지닌 변수나 함수를 보여주는 함수
print(dir([ ]))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(dir({}))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# 6. divmod : a를 b로 나눈 몫 과 나머지를 튜플로 반환
print(divmod(7,3)) #결과 튜플 반환 #몫 2 나머지 1

# 7. enumerate(리스트/튜플/문자열) : 인덱스 값을 포함한 객체를 반환한다.
#리스트의 요소가 위치한 순서대로 번호표시
for i, name in enumerate(['body','foo','bar']) :
    print(i, name)
    #0 body
    # 1 foo
    # 2 bar

# 8. eval() : 문자열로 구성된 표현식을 입력받아 문자열을 실행한 결과값 리턴 / 문자열 무시하는 함수
print(eval('1+2')) #3
print(eval("'hi' + 'a'")) #hia
print(eval('divmod(4,3)')) #(1,1)

# 9.filter(함수, 데이터) : 함수내 조건이 충족하면 반환 함수 , list 변환 가능
# 첫번째 인수로 함수 , 두번째 인수로 그 함수에 들어갈 데이터, 참인 것만 묶어서(걸러내서) 리턴
def positive(x) :
    return x > 0

data = [1,-3,2,0,-5,6]
result = filter(positive, data)
print(list(result)) #list() 리스트 타입으로 타입 변환 해주는 함수

# 람다식 함수 , 함수명 = lambda 매개변수1,매개변수2 : 실행문 ,  js 매개변수 => { }
add = lambda a, b : a + b #return 이라는 명령어가 없어도 결과값이 리턴 된다.
print(add(3,4)) #7
#filter 와 람다식 활용
result = filter(lambda x : x > 0, data) #JS : data.filter(x => x > 0 )
print(list(result))

# 10. map(함수, 데이터) : 함수내 실행문 결과를 반환 함수 , list 타입 변환 가능
result = map(lambda x : x*2 , data)
print(list(result)) #[2, -6, 4, 0, -10, 12]

# 11. hex : 정수를 입력받아 16진수 문자열로 변환하여 리턴
print(hex(234)) #0xea
print(hex(3)) #0x3

# 12 id(객체) : 객체를 입력받아 객체의 고유 주솟값(레퍼런스)를 반환 하는 함수
a = 3
print(id(3))
#140720978790904
print(id(a))
#140720978790904
b = a
print(id(b))
#140720978790904

# 13 input() : 사용자 입력을 받는 함수
# a = input() #입력
print(a) #입력한값 출력
# b = input("Enter : ") #입력 인수로 "Enter : " 문자열 전달
print(b) #입력받은 인수 출력

# 14 int() : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환 하는 함수
a= int('3')
print(a) #정수 3 출력
print(int(3.4)) #소수점 제외 3 출력
print(int('11',2)) #int(x,raidx) x를 10진수로변환하여 리턴 #3
print(int('1A',16)) #16진수로 표현된 1A를 출력 #26

# 15 isinstance(객체, 클래스) : 입력받은 객체가 그 클래스의 인스턴스인지 판단하여 TRUE / FALSE를 리턴
class Person : pass # Person 클래스생성

a = Person() #Person클래스의 a 인스턴스 생성
print(isinstance(a, Person)) # a인스턴스가 Person클래스 의 인스턴스인지 확인 #True
b = 3
print(isinstance(b, Person)) # b인스턴스가 Person클래스 의 인스턴스인지 확인 #False

# 16 len(s) : 요소의 전체 개수를 반환 하는 함수
print(len("python")) #6
print(len([1,2,3])) #3
print(len((1,'a'))) #2

# 17 list() : 반복 가능한 데이터를 입력받아 리스트로 만들어 반환하는 함수 / 리스트로 타입 변환
print(list("python")) #['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3))) #[1,2,3]
a = [1,2,3] #a에 리스트 [1,2,3] 대입
b = list(a) #b 변수에 리스트 타입변환 a 대입
print(b) # 출력 결과 [1, 2, 3]

# 18 max() : 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴 / 최댓값 반환
print(max([1,2,3])) #3
print(max("python")) #y 문자일 경우 유니코드 값이 가장 큰 문자를 리턴

# 19 min() : 인수로 반복 가능한 데이터를 입력받아 최솟값 반환
print(min([1,2,3])) #1
print(min("python")) #h 문자열의 경우 유니코드 값이 가장 작은 문자를 리턴

# 20 oct() : 정수를 8진수 문자열로 바꾸어 반환 하는 함수
print(oct(34)) #0o42
print(oct(12345)) #0o30071

# 21 open() : 파일 이름과 읽기 방법을 입력받아 파일 객체를 반환 하는 함수
# f = open("names.txt" , 'r') #r , w ,a

#  22 ord() : 문자의 유니코드 숫자 값을 리턴하는 함수
a = ord('a')
print(a) # 97
print(ord('가')) # 44032

# 23 pow(x,y) : x를 y제곱한 결괏 값을 리턴 하는 함수
print(pow(2,4)) # 16
print(pow(3,3)) # 27

#24 range([start],stop,[step]) : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴
print(list(range(5))) #[0, 1, 2, 3, 4] #0부터 5개 반환
print(list(range(5,10))) #[5, 6, 7, 8, 9] #5부터 10까지
print(list(range(1,10,2))) #[1, 3, 5, 7, 9] #1부터 9까지 2씩 증가하며
print(list(range(0,-10,-1))) #[0, -1, -2, -3, -4, -5, -6, -7, -8, -9] #0부터 -9까지 -1씩 감소하며

#25 round() : 숫자를 입력받아 반올림해주는 함수
print(round(4.6)) #5
print(round(4.2)) #4
print(round(5.678,2)) #5.68 소수점 2자리까지 반올림하여 표시

#26 sorted() : 데이터를  정렬한 후 그결과를 리스트로 반환하는 함수
print(sorted([3,1,2,])) #[1, 2, 3]
print(sorted(['a','c','b'])) #['a', 'b', 'c']
print(sorted("zero")) #['e', 'o', 'r', 'z']
print(sorted((3,2,1))) #[1, 2, 3]

#27 str() : 문자열 형태로 객체를 변환 하는 함수
print(str(3)) #"3"
print(str('hi')) #"hi"

#28 sum() : 입력받은 데이터의 합을 반환 하는 함수
print(sum([1,2,3])) #6
print(sum([4,5,6])) #15

#29 tuple() : 반복가능한 데이터를 튜플로 바꾸어 반환 하는 함수. 튜플일 경우 그대로 튜플 반환
print(tuple("abc")) #('a', 'b', 'c')
print(tuple([1,2,3])) #(1, 2, 3)
print(tuple((1,2,3))) #(1, 2, 3)

#30 type() : 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc")) #<class 'str'> : 문자열 자료형
print(type([])) #<class 'list'> : 리스트 자료형
print(type(open("test", "w"))) #<class '_io.TextIOWrapper'> : 파일 자료형

#31 zip() : 동일한 개수로 이루어진 데이터들을 묶어서 반환하는 함수
print(list(zip([1,2,3],[4,5,6]))) #[(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9]))) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc","def"))) #[('a', 'd'), ('b', 'e'), ('c', 'f')]