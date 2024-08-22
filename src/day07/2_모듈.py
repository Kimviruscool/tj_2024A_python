# 2_모듈.py

import mod1
#[1] #import 모듈이름 :
    #모듈이름 .함수명()

mod1.add(3,4)

#[2] from 모듈이름 import 함수명 , 함수명
from mod1 import sub
sub(3,4)

#[3] from 모듈이름 import *
from mod1 import *
add(3,4)
sub(4,1)

#[4]
import mod2
print(mod2.PI) #3.141592

a = mod2.Math()
# print(a) #<class 'mod2.Math'>
print (a.solv(2) ) #12.566368

print( mod2.add(3,4) )

from mod2 import Math, PI
print(PI)
print(Math)

#[5]
from src.day06.Task6 import User
s = User('kim','30')
print(s)