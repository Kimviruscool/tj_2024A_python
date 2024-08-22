#main.py

'''
CSV파일 다루기
파일 : 인천광역시_부평구_인구현황.csv
[조건1] 부평구의 동(행) 마다 Region 객체 생성생성해서 리스트 담기
[조건2] Region 객체 변수
[조건3] 모든 객체를 리스트에 담은 상태에서 모든 객체의 정보를 f포메팅 으로
    console 창에 출력하시오
[조건4] 출력시 동 마다 남 여 비율 계산해서 출력하시오.
출력예시 : 동 : 부평동1동 , 총인구수 : 35141 남자인구수 : 16835  여자인구수 : 18306 총 세대수 : 16861  남자 비율 계산 함수 59% 여자 비율 계산 함수 : 41%
'''
from region import *

data = []

def dataRead():
    f = open('인천광역시_부평구_인구현황.csv', 'r')
    db = f.read()
    lines = db.split("\n")
    for i in lines :
        if i :
            cols = i.split(",")
            region = Region(cols[0],cols[1],cols[2],cols[3],cols[4])
            data.append(region)
    f.close()
    return data

if __name__ == "__main__" :
    print('--start--')
    data = dataRead()
    for d in data [1: -1]:
        mpcent = int(100 * (int(d.mpc) / int(d.apc)))
        gpcent = int(100 * (int(d.gpc) / int(d.apc)))
        print(f'동이름 : {d.adress:5s} 총인구수 : {d.apc:5s} 남자인구 : {d.mpc:5s} 여자인구 : {d.gpc:5s} 총 세대수 : {d.spc:5s} 남자비율 : {mpcent}% 여자비율 : {gpcent}%')