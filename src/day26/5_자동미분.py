# day26 > 5_자동미분.py # p45
'''
    - 함수(function)
        - 수학 : 어떤 집합의 각 원소를 다른 어떤 집합의 유일한 원소에 대응시키는 이항 관계
        - *프로그래밍 함수 : 어떠한 코드집합에 매개변수(N개)를 대입하고 결과변수(1개) 를 받는 구조
    - 예시
            x = 3
    -----   --------
    |     x + 4    |
    ------  --------
            y = 7
    -  (수학) 일차 함수
        x       y
        1 ----> 1
        2 ----> 4
        3 ----> 6

    - 기울기 : 기울기 정도  #  y증가량/x증가량 # 두 점의 x 축 증가 와 y축 증가를 나눈 값
        -> 기울기 계산식 : ( x , y )    ( a , b )  # ( x -> a 증가량 )  # ( y -> b 증가량 )
        예]  ( -2 , 0 )   ( 0 , 3 )   #  기울기 = 3 / 2
        예]  ( -3 , 1 )   ( 3 , -2 )  #  기울기 = -3 / 6

    - 미분 : 미세한 부분
        - 실제 y(종속변수) , 예측 y --> 평균제곱오차 # 딥러닝 : 더 복잡하게 계산

    - 일차 방정식 구하는 방법
        기울기 m , 점(지나는점) xy , ab
        1. m = y증가량/x증가량
        2. m = ( y - b ) / ( x - a )
        3  분모 소분  #   ( x - a ) * m = ( y - b ) / ( x - a ) * ( x - a )
        4. m(x-a) = ( y - b )
        5. m(x-a) + b = y
        6. y = m(x-a) + b
            - 기울기 3 , 점 :( 1 , 2 )
            y = 3(x-1) + 2
            y = 3x - 3 + 2
            y = 3x - 1

    - 일차 방정식  : y = ax+b
        - b(y절편)  # y절편 이란 : x축이 0 일때 y의 값  # x절편 이란? y축이 0 일때 x축의 값
        - Y = 3X - 2
            X = 0   계산식 : 3*0 - 2   Y = -2
            X = 1   계산식 : 3*1 - 2   Y =  1
'''

#p.45
#1. 텐서플로 모듈 호출
import tensorflow as tf
from numpy.ma.core import shape
from tensorflow.python.ops.losses.losses_impl import mean_squared_error

#2. 선형 관계를 갖는 데이터 샘플 생성 #Y = 3x - 2
    #1. 텐서프롤의 랜덤 숫자 생성 객체 선언 # 시드값은 아무거나
g = tf.random.Generator.from_seed(2020) #시드란 : 랜덤 생성할때 사용되는 제어 정수값
    #2. 랜덤 숫자 생성 객체를 이용한 정규분포 난수를 10개 생성 해서 벡터(리스트) X에 저장한다.
    #.normal(shape=(축1,축2,축3))
x = g.normal(shape=(10,))
y = 3 * x - 2

print("X:", x.numpy()) #독립변수 피처
print("Y:", y.numpy()) #종속변수 타겟

#3. Loss 함수 정의 # 손실 함수(평균 제곱 오차) 를 정의하는 함수
def cal_msg(X,Y,a,b):
    Y_pred = a * X + b #Y값 종속(예측) = 계수(기울기) a * X(피처) + 상수항(Y절편)
    squared_error = (Y_pred - Y) ** 2 #예측 y와 실제 y간의 차이의 제곱을 계산 (오차제곱)
    mean_squared_error = tf.reduce_mean(squared_error) #모든 오차 제곱의 평균을 계산 하여 반환
    print(mean_squared_error)
    return mean_squared_error

#4. tf.GradientTape로 자동 미분 과정을 기록
    # a 와 b를 미세하게 변경하면서 반복적으로 계산하여 손실을 최소화 하는 값을 찾는다.
a = tf.Variable(0.0)
b = tf.Variable(0.0)

EPOCHS = 200 #계산횟수

for epoch in range(1, EPOCHS + 1): #1 ~ 200까지 (200회 반복)
    with tf.GradientTape() as tape: #iwth 안에 있는 계산식들을 모두 기록하는 역할
        mse = cal_msg(x,y,a,b) #위에서 정의한 손실함수를 계산한다.

    #기울기 계산 #tape.gradient()를 이용하여 mse 에 대한 a와 b의 미분값(기울기)를 구한다.
    grad = tape.gradient(mse,{'a':a,'b':b}) #mse에 대한 a와 b를 딕셔너리 반환한다.
    d_a,d_b = grad['a'],grad['b']
    
    #.assign_sub() 텐서플로변수에 매개변수를 원본값에서 뺀 값으로 변수값을 수정하는 함수
    a.assign_sub(d_a * 0.05) #현재값의 5% 차감
    b.assign_sub(d_b * 0.05)
    
    if epoch % 20 == 0: #20번 마다 #epoch = 반복횟수 #mse : 평균제곱오차 #a계수 #b상수항
        print(f"EPOCH {epoch} - MSE : {mse:.4f} --- a : {a.numpy():.4f} --- b : {b.numpy():.4f}")