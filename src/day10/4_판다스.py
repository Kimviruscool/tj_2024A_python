# 4_판다스.py p.112
# - 테이블형태 다룰수 있는 라이브러리
# 1차원 구조 : Series , 2차원 : DataFrame, 3차원 : Panel
# - [설치]
# - [모듈] import pandas as pd # pd별칭
import pandas as pd


print(pd.__version__) # 2.2.2
print(type(pd)) #<class 'module'>

#[1] Series(리스트) : 1차원 자료구조 객체, 인덱스 0부터 시작

data1 = [10,20,30,40,50] # 리스트 선언
sr1 = pd.Series(data1) # Series 객체 생성
print(sr1)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

data2 = ['1반','2반','3반','4반','5반'] #리스트
sr2 = pd.Series(data2)
print(sr2)
# 0    1반
# 1    2반
# 2    3반
# 3    4반
# 4    5반
# dtype: object

sr3 = pd.Series([101,102,103,104,105])
print(sr3)
# 0    101
# 1    102
# 2    103
# 3    104
# 4    105
# dtype: int64

sr4 = pd.Series(['월','화','수','목','금'])
print(sr4)
# 0    월
# 1    화
# 2    수
# 3    목
# 4    금
# dtype: object

#인덱스 속성
sr5 = pd.Series(data1, index=[1000,1001,1002,1003,1004])
print(sr5)
# 1000    10
# 1001    20
# 1002    30
# 1003    40
# 1004    50
# dtype: int64

sr6 = pd.Series(data1, index=data2)
print(sr6)
# 1반    10
# 2반    20
# 3반    30
# 4반    40
# 5반    50
# dtype: int64

sr7 = pd.Series(data2, index=data1)
print(sr7)
# 10    1반
# 20    2반
# 30    3반
# 40    4반
# 50    5반
# dtype: object

sr8 = pd.Series(data2, index=sr4)
print(sr8)
# 월    1반
# 화    2반
# 수    3반
# 목    4반
# 금    5반
# dtype: object

#Series 인덱싱
#경고 : 인덱스를 0 이 아닌 다른 데이터를 사용하고 있으므로 인덱싱에서 경고 , 해결방안 .iloc
print(sr8.iloc[2]) #3반 iloc : integer location : 정수로 인덱스 나타내겠다.
print(sr8['수']) #3반
print(sr8.iloc[-1]) #5반

#Series 슬라이싱
print(sr8[0:4]) #0에서부터 4개까지
# 월    1반
# 화    2반
# 수    3반
# 목    4반
# dtype: object

#Series 인덱스 구하기 index
print(sr8.index)
# Index(['월', '화', '수', '목', '금'], dtype='object')

#Series 값 구하기 values
print(sr8.values)
#['1반' '2반' '3반' '4반' '5반']

# Series 원소가 숫자 덧셈
print(sr1+sr3)
# 0    111
# 1    122
# 2    133
# 3    144
# 4    155
# dtype: int64

#Series 원소가 문자열이면 문자열 연결 수행
print(sr4+sr2)
# 0    월1반
# 1    화2반
# 2    수3반
# 3    목4반
# 4    금5반
# dtype: object

data_dic = {'year' : [2018,2019,2020], 'sales' : [350,400,1099]}
#딕셔너리 를 이용한 생성
df1 = pd.DataFrame(data_dic)
print(df1)
#    year  sales
# 0  2018    350
# 1  2019    400
# 2  2020   1099

# 2차원리스트를 이용한 생성
df2 = pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]],index = ['중간고사','기말고사'], columns= data2[0:3])
print(df2)
#         1반    2반    3반
# 중간고사  89.2  92.5  90.8
# 기말고사  92.8  89.9  95.2

data_list =  [['20201101','Hong', '90' , '95'], ['20201102','kim','93','94'],['20201103','Lee','87','97']]
df3 = pd.DataFrame(data_list)
print(df3)
#           0     1   2   3
# 0  20201101  Hong  90  95
# 1  20201102   kim  93  94
# 2  20201103   Lee  87  97

df3.columns= ['학번','이름','중간고사','기말고사']
print(df3)
#          학번    이름 중간고사 기말고사
# 0  20201101  Hong   90   95
# 1  20201102   kim   93   94
# 2  20201103   Lee   87   97

print(df3.head(2))
#          학번    이름 중간고사 기말고사
# 0  20201101  Hong   90   95
# 1  20201102   kim   93   94

print(df3.tail(2))
#          학번   이름 중간고사 기말고사
# 1  20201102  kim   93   94
# 2  20201103  Lee   87   97

print(df3['이름'])
# 0    Hong
# 1     kim
# 2     Lee
# Name: 이름, dtype: object


# CSV로 저장
df3.to_csv('score.csv', header='False')

# CSV 에서 불러오기
df4 = pd.read_csv('score.csv', encoding='utf-8',index_col=0,engine='python')
print(df4)
#          학번    이름  중간고사  기말고사
# 0  20201101  Hong    90    95
# 1  20201102   kim    93    94
# 2  20201103   Lee    87    97

