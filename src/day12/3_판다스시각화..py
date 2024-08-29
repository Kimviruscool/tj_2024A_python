# p.124
from idlelib.iomenu import encoding

import matplotlib.pyplot as plt
import pandas as pd

# day= [2015,2016,2017,2018,2019,2020]
# data = [[500,450,520,610],
#         [690,700,820,900],
#         [1100,1030,1200,1380],
#         [1500,1650,1700,1850],
#         [1990,2020,2300,2420],
#         [1020,1600,2200,2550]]
#
#
# dt_tbl = pd.DataFrame(data, index=day ,columns=['1분기','2분기','3분기','4분기'])
# dt_tbl.to_csv("dbtbl.csv", encoding='utf-8', mode='w', index=True)
#
# # print(dt_tbl)
#
# x = range(0, len(data[1]))
#
# for i in data :
#     plt.plot(x,i)
#
# plt.title('2015~2020 Quarterly sales')
# plt.xlabel('Quarterly')
# plt.ylabel('sales')
#
# xLabel = ['first','second','third','fourth']
# plt.xticks(x, xLabel, fontsize=10)
#
# yLabel = ['500','1000','1500','2000','2500']
#
#
# plt.legend(['2015','2016','2017','2018','2019','2020'])
# # plt.show()

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