"""
Напишите программу, которая принимает на вход
вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""

number = str(input("Введите число: "))
sumNumber = 0
for i in range(len(number)):
    if number[i] not in [".", ","]:
        sumNumber += int(number[i])
print(f"Сумма цифр числа {number} равна {sumNumber}")