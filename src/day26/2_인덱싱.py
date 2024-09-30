#2_인덱싱.py #텐서플로.p36
import tensorflow as tf
from tensorboard.compat.tensorflow_stub.tensor_shape import vector

'''
-인덱싱
    - 원소가 저장된 순서 번호
    - 0번 시작하고 마지막 인덱스 -1
-슬라이싱
    - [시작 : 끝]
'''

#1. 벡터
vec = tf.constant([10,20,30,40,50])
print(vec)
print(vec[0]) #스칼라 #tf.Tensor(10, shape=(), dtype=int32)
print(vec[0].numpy()) #10
print(vec[-1]) #스칼라 #tf.Tensor(50, shape=(), dtype=int32)
print(vec[0:3]) #0 ~ 2 #tf.Tensor([10 20 30], shape=(3,), dtype=int32)

#2. 행렬
mat = tf.constant([[10,20,30],[40,50,60]])
print(mat[0,2]) #[행인덱스 , 열인덱스] # 첫번째 행 , 세번째열 # 스칼라 #tf.Tensor(30, shape=(), dtype=int32)
print(mat[0, :]) #행(슬라이싱), 열(슬라이싱) #첫번째 행 , 전체 열 [ : ] #벡터 #tf.Tensor([10 20 30], shape=(3,), dtype=int32)
print(mat[:,1]) #전체 행 [:], 두번째열(슬라이싱) #벡터 #tf.Tensor([20 50], shape=(2,), dtype=int32)
print(mat[:,:]) #전체 행 , 전체 열 [:] #벡터 #tf.Tensor([[10 20 30] [40 50 60]], shape=(2, 3), dtype=int32)

#3. 3차원 텐서
tensor = tf.constant( #(행렬2개, 벡터 2개, 스칼라 3개) # (높이=2 , 행=2, 열=3)
    [ #축1 - 고차원 텐서 (3차원 리스트)
        [ #축2 - 행렬 (2차원 리스트)
            [#축3 - 벡터 (1차원 리스트)
                10,20,30],[40,50,60]
        ],

        [
            [-10,-20,-30],[-40,-50,-60]
        ]
    ]
)
print(tensor)
print(tensor[0,:,:]) #첫번째 축1 에서 첫번째 인덱스, 축2 에서 전체인덱스 , 축3에서 전체인덱스 #행렬 # (2,3)
print(tensor[:,0:2,0:2]) #축1(전체),축2(0~1),축3(0~1) #(2,2,2)

#연습
#1. 벡터
vector = tf.constant([10,20,30,40,50])
#첫번째 스칼라(요소) 출력하기
print(vector[0].numpy()) #10

#마지막 에서 두번째 스칼라(요소) 출력하기
print(vector[-2].numpy()) #50

#앞에서 3개 요소 슬라이싱
print(vector[0:3].numpy()) #[10 20 30]

#뒤에서 4개 요소 슬라이싱
print(vector[-4:].numpy()) #[20 30 40 50]

#2. 행렬 #2D
matrix = tf.constant( [ [1,2,3],[4,5,6],[7,8,9] ] )

#첫번째 행 ,두번째 열 요소 인덱싱
print(matrix[0,1].numpy()) #2

#세번째 행 ,첫번째 열 요소 인덱싱
print(matrix[2,0].numpy()) #7

#첫번째 행 전체 슬라이싱
print(matrix[0,:].numpy()) #[1 2 3]

#두번째 열 전체 슬라이싱
print(matrix[:,1].numpy()) #[2 5 8]


#3. 3차원 텐서 #3D
tensor = tf.constant( [ [ [1,2],[3,4] ] , [ [5,6],[7,8] ] ] )

#가장 첫번째 요소 인덱싱 1
print(tensor[0,0,0].numpy()) #1

#가장 마지막 요소 인덱싱 8
print(tensor[-1,-1,-1].numpy()) #8

#첫번째 행렬 슬라이싱
print(tensor[0,:,:].numpy()) #[[1 2] [3 4]]

#두번째 행렬의 첫번째 행 슬라이싱
print(tensor[1,0,:].numpy()) #[5 6]