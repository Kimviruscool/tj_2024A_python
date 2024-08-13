# 2_딕셔너리.py
# - key 와 value 를 한쌍으로 가지는 자료형
# - {key1 : value1 , key2 : value2 , key3 : value3} 형태

#(1) 딕셔너리 형태
dic = {'name' : 'pey' , 'phone' : '010-9999-1234', 'birth' : '1118'}
a = {1 : 'hi'}
a = {'b' : [1,2,3]}

#(2) 딕셔너리 의 쌍 추가 , 삭제
#[1] 추가 , 수정
# 딕셔너리 내 존재하지 않는 key 이면 쌍 추가
# 딕셔너리 내 존재하는 key 이면 value 수정
dic['addr'] = '인천시' #변수명['key'] = 새로운값(초기값)
print(dic) # {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118', 'addr': '인천시'}
dic['name'] = 'kim' #변수명['key'] = 새로운값(수정값)
print(dic) # {'name': 'kim', 'phone': '010-9999-1234', 'birth': '1118', 'addr': '인천시'}

#[2] 삭제
del dic['addr'] #del 변수명['key'], 딕셔너리 내 존재하는 key 이면 쌍 삭제
print(dic)#{'name': 'kim', 'phone': '010-9999-1234', 'birth': '1118'}
# del dic['age'] #KeyError: 'age' , 딕셔너리 내 존재하지 않는 key 이므로 예외(Error) 발생

#(3) 딕셔너리에서 key를 이용한 value 추출
print(dic['name']) #kim 출력 , 딕셔너리 내 존재하는 key 이면 value 반환
# print(dic.name) #AttributeError: 'dict' object has no attribute 'name' : 객체가 아니라서 불가능
# print(dic['age']) #KeyError: 'age' : 딕셔너리 내 존재하지 않는 key 이면 예외(Error) 발생
print(dic['phone']) #010-9999-1234 출력 , 딕셔너리 내 존재하는 key('phone') 이므로 value('010-9999-1234') 반환

#(4) 딕셔너리 만들때 주의 할점
    #1. 중복된 key의 이름을 가질 수 없다, value는 가능
a = {1 : 'a', 1 : 'b'}
print(a) #{1 : b} , key는 중복이 불가능 하므로 마지막 쌍이 적용된다.
    #2. 리스트 타입으로는 key로 사용할 수 없다, key가 변화하는 값인지 변화하지 않는 값인지가 중요하다.
# a = { [1,2] : 'hi'}
# print(a) #TypeError : unhashtable type : 'list'

#(5) 딕셔너리 관련 함수
#1. keys() : 딕셔너리 내 모든 key를 리스트로 반환
print(dic.keys()) #dict_keys(['name', 'phone', 'birth']) , py3.0이상 객체 반환

#2. list(객체) : 객체를 리스트로 변환 해서 반환하는 함수
print(list(dic.keys())) #['name', 'phone', 'birth'] 객체화

#.3 values() : 딕셔너리 내 모든 values 를 모아 객체로 반환 , py3.0이상 객체 반환
print(dic.values())
print(list(dic.values())) #['kim', '010-9999-1234', '1118']

#4.items() : 딕셔너리 내 모든 쌍을 튜플로 묶은 객체로 반환 함수
print(dic.items()) #dict_items([('name', 'kim'), ('phone', '010-9999-1234'), ('birth', '1118')])
print(list(dic.items())) #[('name', 'kim'), ('phone', '010-9999-1234'), ('birth', '1118')]

#5. .get('key') : 딕셔너리 내 key 해당 하는 value 반환 함수
print(dic.get('name')) #kim, 만일 딕셔너리내 존재하는 key이면 Value 반환
print(dic.get('age')) #None , 만일 딕셔너리내 존재하는 key가 아니면 None 반환 , dic['age'] 보다 조금더 안전한 방법 일것 같다.

#6 key in 딕셔너리 변수명 : 딕셔너리 내 key의 존재 여부 true/false 로 반환 함수
print('name' in dic) # true 존재
print('age' in dic) #false 비존재

#7. clear() : 딕셔너리 내 모든 쌍을 삭제한다.
dic.clear()
print(dic) # {} #