# 4_불.py #boolean
# - 불 자료형 : 참 True / 거짓 False 를 나타내는 자료형
# Ture : 참을 의미 / False : 거짓을 의미 , * 첫 글자는 대문자 로 시작

'''
"Python" Ture   " "      False
[1,2,3]  True    [ ]     False
(1,2,3)  True    ( )     False
{'a',1}  True    { }     False
1        True    0       False
                 None    False
'''

#(1) 불 자료형
a = True
b = False
#(2) type(자료) : 자료의 타입을 반환 하는 함수
print(type(a)) #<class 'bool'>
print(type(b)) #<class 'bool'>
print( 1 == 1) #True
print( 2 > 1 ) #True
print( 2 < 1 ) #False
#(3) 자료형의 참과 거짓
#(4) 불(bool) 의 연산 : 해당 자료의 불타입 T/F 반환 함수
print(bool('python')) #True
print(bool('')) #False
print(bool([1,2,3])) #True
print(bool([])) #False
print(bool(0)) #False
print(bool(1)) #True