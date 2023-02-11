# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

num = int(input("Введите число: "))
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")