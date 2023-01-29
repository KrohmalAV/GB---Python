"""
Задайте список из N элементов, заполненных числами
из промежутка [-N, N]. Найдите произведение элементов
на указанных позициях. Позиции хранятся в файле file.txt
в одной строке одно число.
"""
import random
number = int(input("Введите натуральное число: "))
listNumbers = list()
for i in range(number*2+1):
    listNumbers.append(random.randint(-number, number))
print(listNumbers)

positions = open("Homework/DZSEM2/file.txt", "r")
position1 = int(positions.readline())
position2 = int(positions.readline(2))
positions.close()
multi = listNumbers[position1] * listNumbers[position2]
print(f"Произведение элементов на позициях {position1} ({listNumbers[position1]}) и {position2} ({listNumbers[position2]}) равняется {multi}")
