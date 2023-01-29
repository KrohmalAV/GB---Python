"""
Реализуйте алгоритм перемешивания списка.
"""

import random
def createList(N, min, max):
    createList = list()
    for i in range(N):
        createList.append(random.randint(min, max))
    return createList

def mixList(List):
    for i in range (len(List)):
        x = int(random.randint(0, len(List)-1))
        List[i], List[x] = List[x], List[i] 

N = int(input("Введите размер списка: "))
Min = int(input("Введите минимальное значение элемента в списке: "))
Max = int(input("Введите максимальное значение элемента в списке: "))
List = createList(N, Min, Max)
print(f"   Список начальный: {List}")
mixList(List)
print(f"Список перемешанный: {List}")
    