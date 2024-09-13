#3_로지스틱성능평가.py

'''
오차행렬
    -실제 클래스(값) 은 행
    -예측 클래스(값) 은 열
        TN      FP
        FN      TP

        3       1
        3       3

        양성 (1) , 음성 (0)
    - TP : 실제 값이 양성 이고 예측 값도 양성 인 경우    (3)
    - TN : 실제 값이 음성 이고 예측 값도 음성 인 경우    (3)
    - FP : 실제 값이 음성 이고 예측 값이 양성 인 경우    (1)
    - FN : 실제 값이 양성 이고 예측 값이 음성 인 경우    (3)
    
    
    정밀도 계산식 : 예측 성능을 더 정밀하게 평가하기 위해 참(tp) 인것 의 비율 계산
                    #양성 으로 예측한 값들 중에서 실제 양성 비율
    
    
              TP            3
    정밀도 = ------    /    --------
            FP+TP           1+3
    
    
    - 재현율 계산식 : 실제 Positive인 데이터 중 인것 중에서 참[TP]인 비율 계산 #민감도
                        #실제 양성인 값 중에서 모델이 양성 으로 정확 하게 예측한 비율
                        
                 TP              3
    재현율 =  ---------- /     -------
                FN+TP           1+3
                
                
    F1 스코어 : 정밀도와 재현율을 결합한 평가지표 , 정밀도와 재현율이 서로 상층 관계인 문제점을 고려하여 정확한 평가
                # 정밀도와 재현율의 조화 평균 으로 서로 간의 균형을 측정 지표
                
                    정밀도 * 재현율              0.75 * 0.75
    F1 스코어 = 2 X --------------- =   / 2 X ------------------
                    정밀도 + 재현율              0.75 + 0.75


    ROC 기반의 AUC 스코어 : 실제 Negative 인 데이터를 Positive 로 거짓으로 예측한 비율
                            #ROC 이란 :  FPR 이 변 할때 TPR 이 어떻게 변하는지 나타내는 곡선이다.

               FP                           1
    FPR = --------------    /   FPR = --------------
            FP + TN                      1 + 3
'''
#실제 시험 합격목록
y_ture = [0,0,0,1,1,0,1,1,1,1]
#시험 예측 합격 목록
y_pred = [0,0,0,0,0,1,0,1,1,1]

#[1] 오차 정렬 함수
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_ture, y_pred)) #오차행렬
#[2] 정밀도 함수
from sklearn.metrics import precision_score #정밀도 구해주는 함수
print(precision_score(y_ture, y_pred)) #0.75 #75% #높을수록 정밀하다.
#[3] 재현율 함수
from sklearn.metrics import recall_score
print(recall_score(y_ture,y_pred)) #0.5 # 50% #높을수록 잘 재현 되어있다.
#[4] F1 스코어 함수
from sklearn.metrics import f1_score
print(f1_score(y_ture, y_pred)) #0.6 # 60% #높을수록 정밀도와 재현율의 균형이 잘 맞춰져 있다.
#[5] ROC 기반 AUC 스코어 함수
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_ture , y_pred)) #0.625 #1에 가까울수록 좋은 성능 이다.