# 5_2장되새김문제.py

#Q1 평균 점수 구하기

a = 80
b = 75
c = 55
d = a+b+c
print(d/3)
#Q2 홀수,짝수 판별하기
a2 = 13
if a2%2 ==0 : print(a2, '은 짝수입니다.')
else : print(a2, "은 홀수입니다.")
#Q3 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:13]
print(yyyymmdd)
print(num)
#Q4 주민등록번호 인덱싱
print(pin[7])
#Q5 문자열 바꾸기
a5 = "a:b:c:d"
b5 = a5.replace(":","#")
print(b5)
#Q6 리스트 역순 정렬하기
a6 = [1,3,5,4,2]
a6.sort()
a6.reverse()
print(a6)
#Q7 리스트를 문자열로 만들기
a7 = ['Life','is','too','short']
result = "".join(a7)
print(result)
#Q8 튜플 더하기
a8 = (1,2,3)
a8 = a8 + (4,)
print(a8)
#Q9 딕셔너리의 키 (키 : 값 형태)
a9 = dict()
a9['name'] = 'python'
print(a9)
a9[('a',)] = 'pthon'
print(a9)
# a9[[1]] = 'python' #예외 발생 : 키는 편하지 않는 값인데 [1] 은 변하는 값이기 떄문에 사용불가능
# print(a9)
a9[250] = 'python'
print(a9)
#Q10 딕셔너리 값 추출하기
a10 = {'A':90 , 'B':80, 'C':70}
result10 = a10.pop('B')
print(a10)
print(result10)
#Q11 리스트에서 중복 제거하기
a11 = [1,1,1,2,2,3,3,3,4,4,5]
aSEt = set(a11)
b = list(aSEt)
print(b)
#Q12 파이썬 변수
a = b = [1,2,3]
a[1] = 4
print(b)
#동일한 값을 가지는 a , b 변수에서 a[1] 째 2를 4로 수정하면 b[1] 째 2도 같이 수정된다. 따라서 결과 : [1,4,3] 이 출력된다.