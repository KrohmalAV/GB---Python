# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
def createList(lenList):
    createList = []
    for i in range(lenList):
        createList.append(random.randint(0, 10))
    return createList

def multiList(list1):
    multiList = []
    for i in range(int((len(list1)+1)/2)):
        multiList.append((list1[i]*list1[-1-i]))
    return multiList

lenList = int(input("Введите размер списка: "))
myList = createList(lenList)
print(myList)
print(multiList(myList))
