# task7 > Main.py

from User import *

names = []

def nameCreate():
    global names  # 전역변수 호출
    addName = input("addName : ")
    addAge = input("addAge : ")

    names.append(User(addName, addAge))
    return


def nameRead():
    global names
    for dic in names :
        print(f'name : {dic.name} age : {dic.age}')
    return


def nameUpdate():
    global names  # 전역변수
    oldName = input("oldName : ")
    for dic in names :
        if dic.name == oldName :
            dic.name = input("newName : ")
            dic.age = input("newAge : ")
            return
    return


def nameDelete():
    global names
    delName = input("delName : ")
    for dic in names :
        if dic.name == delName :
            names.remove(dic)
            return
    return

if __name__ == "__main__" :
    while True:  # 무한루프
        ch = int(input("1.Create 2.Read 3.Update 4.Delete : "))
        if ch == 1:
            nameCreate()

        elif ch == 2:
            nameRead()

        elif ch == 3:
            nameUpdate()

        elif ch == 4:
            nameDelete()