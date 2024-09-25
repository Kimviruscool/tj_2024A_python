#1_텐서플로.py
# 텐서플로 : 텐서(다차원데이터)를 플로(흐름) 에 따라 연산하는 과정을 제공하는 라이브러리
# tensorflow 모듈 설치 :
#[1] 모듈 호출
import tensorflow as tf
from flatbuffers.packer import float32

#[2] 텐서플로2 에서 즉시 실행 모드인지 확인하는 함수
print(tf.executing_eagerly()) #True
#[3] 텐서플로 연산 #연산 결과를 텐서 객체로 반환
a = 1
b = 2
c = tf.math.add(a,b)
print(c) #tf.Tensor(3, shape=(), dtype=int32)
print(type(c)) #<class 'tensorflow.python.framework.ops.EagerTensor'>

#[4] .numpy() : 텐서 객체내 에서 결과값 추출
print(c.numpy()) #3

#[5] 텐서(상수 : 스칼라) #tf.Tensor(값, shape=(배열크기), 타입 )
a = tf.constant(1)
b = tf.constant(2)
print("a : ", a) #a :  tf.Tensor(1, shape=(), dtype=int32)
print("b : ", b) #b :  tf.Tensor(2, shape=(), dtype=int32)
    #2. 랭크 확인
print(tf.rank(a)) #tf.Tensor(0, shape=(), dtype=int32)
    #3. 스칼라 데이터 타입변환 #.cast(스칼라객체 , tf.지원타입)
a = tf.cast(a, tf.float32)
b = tf.cast(b, tf.float32)
print(a.dtype) #<dtype: 'float32'> #tf.Tensor(1.0, shape=(), dtype=float32)
print(b.dtype) #<dtype: 'float32'> #tf.Tensor(2.0, shape=(), dtype=float32)
    #4. 수학적 함수 # .math
#1. 덧셈
c = tf.math.add(a,b)
print(c) #tf.Tensor(3.0, shape=(), dtype=float32)
print(tf.rank(c)) #tf.Tensor(0, shape=(), dtype=int32)
print(a + b)
#2. 뺄셈
print(tf.math.subtract(a,b)) #tf.Tensor(-1.0, shape=(), dtype=float32)
print(a - b)
#3. 곱셈
print(tf.math.multiply(a,b)) #tf.Tensor(2.0, shape=(), dtype=float32)
print(a * b)
#4. 나눗셈
print(tf.math.divide(a,b)) #tf.Tensor(0.5, shape=(), dtype=float32)
print(a / b)
#4-1. 나눗셈(나머지)
print(tf.math.mod(a,b)) #tf.Tensor(1.0, shape=(), dtype=float32)
print(a % b)
#4-2. 나눗셈(몫)
print(tf.math.floordiv(a,b)) #tf.Tensor(0.0, shape=(), dtype=float32)
print(a // b)

#[6] 텐서(1차원 리스트 : 벡터)
import numpy as np

vec1 = tf.constant([10,20,30], dtype=tf.float32) #파이썬 리스트 #tf.Tensor([10 20 30], shape=(원소개수,), dtype=int32)
vec2 = tf.constant(np.array([10,10,10]), dtype=tf.float32)
print(vec1) #tf.Tensor([10 20 30], shape=(3,), dtype=int32)
print(vec2) #tf.Tensor([10 10 10], shape=(3,), dtype=int32)

print(tf.rank(vec1)) #tf.Tensor(1, shape=(), dtype=int32)
print(tf.rank(vec2)) #tf.Tensor(1, shape=(), dtype=int32)

add1 = tf.math.add(vec1,vec2)
print(add1) #tf.Tensor([20 30 40], shape=(3,), dtype=int32)
print(tf.rank(add1)) #tf.Tensor(1, shape=(), dtype=int32)
print(vec1 - vec2)
print(vec1 * vec2)
print(vec1 / vec2)
print(vec1 % vec2)
print(vec1 // vec2)

#벡터내 요소 총합계
print(tf.reduce_sum(vec1)) #tf.Tensor(60, shape=(), dtype=int32)
print(tf.reduce_sum(vec2)) #tf.Tensor(30, shape=(), dtype=int32)

#거듭 제곱
print(tf.math.square(vec1)) #tf.Tensor([100 400 900], shape=(3,), dtype=int32)
print(vec1 ** 2)
#제곱근
print(tf.math.sqrt(vec2)) #tf.Tensor([3.1622777 3.1622777 3.1622777], shape=(3,), dtype=float32)
print(vec2 **0.5)
#브로드캐스팅 연산 
print(vec1 + 1) #tf.Tensor([11. 21. 31.], shape=(3,), dtype=float32)

#[6] 텐서객체(2차원 리스트 : 행렬) #shape=(행개수, 열개수), dtype=int32)
mat1 = tf.constant([[10,20],[30,40]]) #전체를 감싼 대괄호내 원소개수 : 행 개수/백터 갯수 # 내부 대괄호내 원소개수 : 열개수/스칼라개수
print(mat1) # 행 과 열 이라는 축이 2개라서 랭크/차수 : 2
'''
tf.Tensor(
[[10 20]
 [30 40]], shape=(2, 2), dtype=int32)
'''
print(tf.rank(mat1)) #tf.Tensor(2, shape=(), dtype=int32)
#mat2 = tf.stack(벡터,벡터)
mat2 = tf.stack([[1,1],[-1,2]])
print(mat2)
'''
tf.Tensor(
[[ 1  0]
 [-1  2]], shape=(2, 2), dtype=int32)
'''
print(tf.rank(mat2))
#행렬 연산
print(tf.math.multiply(mat1,mat2))
'''
tf.Tensor(
[[ 10   0]
 [-30  80]], shape=(2, 2), dtype=int32)
'''
print(mat1 * mat2)
print(mat1 + mat2) #add
print(mat1 - mat2) #subtract
print(mat1 / mat2) #divide
# print(mat1 % mat2) #오류 #CPU 계산은 %연산자를 지우너하지 않는다. division by zero 조심
print(tf.math.mod(mat1,mat2))
# print(mat1 // mat2) #오류
print(tf.math.multiply(mat1, 3)) #브로드 캐스팅
#행(가로) 열(세로) 곱 연산
print(tf.matmul(mat1,mat2))
'''
tf.Tensor(
[[-10  40]
 [-10  80]], shape=(2, 2), dtype=int32)
'''

'''
인공지능 (AI)
    - 빅데이터 : 많은 자료들
    - 머신러닝 : 자료들의 학습 모델 (사이킷런 라이브러리)
    - 딥러닝 : 복잡한 자료들의 학습 모델 (텐서플로 라이브러리)

텐서플로 자료구조 

스칼라         벡터             메트릭                  텐서  
rank-0        rank-1          rank-2                 rank-3
값            리스트            2차원 리스트            3차원 리스트
차수-0        차수(축)-1        차수(축)-2             차수(축)-3
X            한방향 : X         두방향:가로(X)세로(Y)   세방향:가로(X)세로(Y)높이(Z)
'''