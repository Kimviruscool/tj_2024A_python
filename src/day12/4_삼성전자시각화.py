# 4_삼성전자시각화.py

import matplotlib.pyplot as plt
import pandas as pd

# 실습1 : 삼성전자 의 최근 주가 1년 시세 정보 CSV로 다운로드 받아서 판다스(데이터프레임) 으로 읽어오기
# 정보데이터시스템 : https://www.krx.co.kr/
    #1. 데이터프레임 객체 콘솔 에 출력(CSV - 데이터프레임)
    #2. 삼성전자 종가 최근 1년 시세 중 일자별 막대차트로 표현하시오. 일 X 종가 Y

df = pd.read_csv('data_5209_20240829.csv', encoding='utf-8', engine='python')
print(df['종가'])
print(df['일자'])

#바 차트 생성
y = df['종가']
x = df['일자']

plt.bar(x , y, width=0.4)

plt.title('Samsung stock')
plt.xlabel('YY-MM-DD')
plt.ylabel('c-Price')

plt.show()