# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def listSimpleNum(num):
    listSimpleNum = []
    for i in range(2, num + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            listSimpleNum.append(i)
    return listSimpleNum

def listSimpleMultipliers(num, listSimpleNum):
    listSimpleMultipliers = []
    for i in range(len(listSimpleNum)):
        if num % listSimpleNum[i] == 0:
            listSimpleMultipliers.append(listSimpleNum[i])
    return listSimpleMultipliers 

num = int(input("Введите натуральное число: "))
if num > 1:
    print(listSimpleMultipliers(num, listSimpleNum(num)))
elif num == 1:
    print("[1]")
else:
    print("Эх ты... просили же ввести натуральное число...")