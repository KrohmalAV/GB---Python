# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def num10ToNum2(num10):
    num2 = ""
    while num10 > 0:
        num2 = str(num10 % 2) + num2
        num10 //= 2
    return num2

num10 = int(input("Введите десятичное число: "))
print(f"{num10} => {num10ToNum2(num10)}")