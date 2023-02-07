# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной
# позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def createList(lenList):
    createList = list()
    for i in range(lenList):
        createList.append(random.randint(-10, 10))
    return createList

lenList = int(input("Введите размер списка: "))
myList = createList(lenList)
print(myList)
total = 0
for i in range(1, len(myList), 2):
    total += myList[i]
print(f"Сумма элементов списка c нечетными индексами равна {total}")
