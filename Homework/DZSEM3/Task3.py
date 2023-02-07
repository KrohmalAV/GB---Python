# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
def createList(lenList):
    createList = []
    for i in range(lenList):
        createList.append(random.randint(0, 10000)/100)
    return createList

def diffBalance(myList):
    min = round(myList[0] % 1, 2)
    max = round(myList[0] % 1, 2)
    for i in range(len(myList)):
        if myList[i] % 1 < min:
            min = round(myList[i] % 1, 2)
        elif myList[i] % 1 > max:
            max = round(myList[i] % 1, 2)
    diff = round(max - min, 2)
    return diff

lenList = int(input("Введите размер списка: "))
myList = createList(lenList)
print(myList)
print(f"Разница наибольшей и наименьшей дробной части = {diffBalance(myList)}")
