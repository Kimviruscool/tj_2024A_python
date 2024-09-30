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