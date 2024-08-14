#2_3장되새김문제.py

#Q1 조건문의 참과 거짓
a = "Life is too short, you need python"

if "wife" in a : print("wife") #만약에 a 안에 wife 가있으면 wife출력
elif "python" in a and "you" not in a : print("python") #만약에 a 안에 pyhton이 존재하고 you가 존재하지 않으면 python출력
elif "shirt" not in a : print("shirt") #만약에 shirt 가 a안에 없으면 shirt 출력
elif "need" in a : print("need") #만약에 a 안에 need 가 존재하면 need 출력
else: print("none") #그게아니면 none 출력
#결과  : shirt (shirt 에서 elif 조건이 걸렸기때문에 아래는 출력되지 않는다.)

#Q2 3의 배수의 합 구하기
result = 0
i = 1
while i <= 1000 :
    if i%3 ==0 :
        result += i
    i += 1
print(result)

#Q3 별 표시하기
i = 0
while True:
    i += 1
    if i == 6 : break
    print('*' * i)

#Q4 1부터 100까지 출력하기
for i in range(1,101) :
    print(i)

#Q5 평균 점수 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A :
    total += score
average = total / 10
print(average)
#Q6 리스트 컴프리헨션 사용하기
numbers = [1,2,3,4,5]
result = []
for n in numbers :
    if n % 2 == 1:
        result.append(n*2)
print(result)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)