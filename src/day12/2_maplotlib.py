# day12 > 2_maplotilb.py
# - 파이썬 에서 데이터를 시각화 해주는 패키지
# - 데이터 분석 결과를 시각화 하여 직관적으로 이해하기 위해서 사용
# - 선(라인) 차트 , 바 차트 , 파이(원형)차트, 히스토그램 , 산점도 등등

#[1] 설치
#방법1 : from ~~ import ~~ > 손올려서 설치
#방법2 : 상단 > 파일 > 설정 > 왼쪽메뉴프로젝트 하위 인터프리터
    #alt + insert > matplotlib 검색후 설치
#방법3 : terminal > pip install matplotlib 입력

#[2] 모듈가져오기
import matplotlib
#[3] 버전 확인
print(matplotlib.__version__) #3.9.2
#[4] pyplot 모듈 가져오기
import matplotlib.pyplot as plt

#[1] 라인차트
#1. 차트에 표시할 데이터 샘플 데이터 준비
x = [2016,2017,2018,2019,2020]
y = [350,410,520,695,543]
#2. 라인플롯(선 차트)에 x축과 y축지정하여 라인플롯 생성
plt.plot(x , y)
#3. 차트 제목 지정
plt.title('Annual Sales')
#4. x축 레이블(축 제목) 설정
plt.xlabel('year')
plt.ylabel('sales')
#5. 라인플롯 표시/실행
plt.show()

#[2] 바 차트
#1. 차트에 표시할 데이터 샘플 준비
y1 = [350,410,520,695]
y2 = [200,250,385,350]
x = range(len(y1)) #0부터 y1 길이만큼 리스트 생성 [0,1,2,3]

#2. x축과 y축 데이터를 지정하여 바 차트 생성 #width = 굵기 # color = 색상
plt.bar(x, y1, width=0.7, color = "blue")
plt.bar(x, y2, width=0.7, color = "red", bottom=y1)

#3. 차트 제목 설정
plt.title('Quarterly sales')
#4. x축 레이블 설정
plt.xlabel('Quarters')
#5. y축 레이블 설정
plt.ylabel('sales')
#6. 눈금 이름 리스트 생성
xLabel = ['first','second','third','fourth']
#7. 바 차트의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize=10)
#8.범례 설정 (막대구분 이름 표시)
plt.legend(['chairs','desks'])
#9. 바 차트 표시/실행
plt.show()

#[7] . 산점도 : x축과 y축의 값 관계를 시각화 # 각 데이터 포인트는 두 변수의 값을 x축 y축에 대응시켜 점으로 표현
#1. 데이터 준비
import random
x = [random.random() for _ in range(50)] #50 개의 x축 요소를 난수로 생성한다.
print(x)
y = [random.random() for _ in range(50)] #50 개의 y축 요소를 난수로 생성한다.
print(y)
#2. 산점도 차트 생성
plt.scatter(x , y)
#3. 산점도 차트 출력/실행
plt.show()