"""
Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
"""
number = int(input("Введите натуральное число: "))
if number <= 0:
    print("Нужно было ввести натуральное число")
else:
    multiList = []
    multi = 1
    for i in range(1, number+1):
        multi *= i
        multiList.append(multi)
    print(multiList)
"""
    
number = int(input("Введите натуральное число: "))
if number <= 0:
    print("Нужно было ввести натуральное число")
else:
    multi = 1
    print("[ ", end="")
    for i in range(1, number+1):
        multi *= i
        print(multi, end="  ")
    print("]", end="")
        
    