"""
Задача 9: По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

numder = int(input("Введите целое неотрицательное число N: "))
if numder == 0:
    print(f"{numder}! = 1")
elif numder < 0:
    print(f"Нужно было ввести неотрицательное число")
else:
    sum = 1
    i = 1
    while i <= numder:
        sum *= i
        i += 1
    print(f"{numder}! = {sum}")