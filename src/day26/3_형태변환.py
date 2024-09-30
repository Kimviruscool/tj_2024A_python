#3_형태변환
import tensorflow as tf

#1. 벡터 정의
tensor = tf.constant(range(0,24))
print(tensor) # [0~24] #shape = (24,)

#2. 벡터 > 행렬 변환 #reshape(,변환할텐서, [행, 열]) 텐서 변환
tensor1 = tf.reshape(tensor, [3,8])
#24개 못맞추면 #Input to reshape is a tensor with 24 values, but the requested shape has 16 [Op:Reshape]
print(tensor1) #[[0~7],[8~15,[16~23]] #(3,8)
'''
tf.Tensor(
[[ 0  1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14 15]
 [16 17 18 19 20 21 22 23]], shape=(3, 8), dtype=int32)
'''
# tensor2 = tf.reshape(tensor, [6,4])
tensor2 = tf.reshape(tensor, [-1,4]) #-1 : 어떤 값이 되어도 관계없다.
print(tensor2)
'''
tf.Tensor(
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]], shape=(6, 4), dtype=int32)
'''
#3. 행렬 > 벡터
tensor3 = tf.reshape(tensor2, [-1]) #요소의 개수를 모르기 때문에 -1
print(tensor3) #tf.Tensor([ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23], shape=(24,), dtype=int32)

#4. 벡터 > 3차원 텐서 변환
# tensor4 = tf.reshape(tensor3, [2,3,4])
tensor4 = tf.reshape(tensor3, [-1,3,4])
print(tensor4) #shape=(2, 3, 4), dtype=int32)

#5. 3차원 텐서 > 3차원 텐서 변환 #(2,3,4) > (3,2,4)
tensor5 = tf.reshape(tensor4, [3,2,4])
print(tensor5) #shape=(3, 2, 4), dtype=int32)

#6. 3차원 텐서 > 4차원 텐서 변환 #(3,2,4) > (3,2,2,2)
tensor6 = tf.reshape(tensor5, [3,2,2,2])
print(tensor6) #shape=(3, 2, 2, 2), dtype=int32)

