# day15 > 1_카이검증.py
# 카이검증이란? 
# (독립성 검증)두 변수간의 독립성을 검증
#   예]: 성별과 선호하는 제품 유형간의 연관성
        #남자는 컴퓨터를 좋아하고 , 여자는 핸드폰 좋아한다.
            #1. 설문조사 : 1. 남자 2. 여자    (명목형 변수)
            #2. 설문조사 : 1. 컴퓨터 2. 휴대폰 
# (적합성 검증)관찰된 빈도 분포가 얼마나 예상된 분포와 얼마나 일치하는지 검증
#   예]: 주사위를 여러번 굴렸을때 나오는 빈도가 이론적 으로 예상 되는 빈도와 일치 하는지 확인/검증


#[1] 성별 별로 컨텐츠 선호도 조사
#설문조사를 통해 귀하는  ~~~~
# (1) 1. 남자 2. 여자 (명목형) 
# (2) 1.스포츠 2.드라마

#[2] 자료 수집 
'''
    -설문 조사 결과

        스포츠     드라마
    남   50명      30명
    여   20명      40명
'''
설문결과 = [[50,30],[20,40]]

# [3] 모듈 호출
import scipy.stats as stats
# [4] 카이 검증
    #파이썬 문법 : 변수1, 변수2, 변수3 = 함수명() #함수의 리턴값 항상 1개이다. 여러개 일때 주로 튜플()

통계량 , p값 , 자유도 , 기대빈도표 = stats.chi2_contingency(설문결과) #contingency() 유연성 뜻

# [5] 카이 검증 결과
print(통계량)#10.529166666666667 #검증한 두 집단의 빈도 차이를 나타내는 값
print(p값) #0011750518530845063
print('성별과 컨텐츠 선호도가 독립적일때 예상되는 빈도표')
print(기대빈도표)#[[40. 40.] [30. 30.]]

if p값 <= 0.05 :
    print("해당 설문은 유의미 하다.")
else :
    print("해당 설문은 무의미 하다.")