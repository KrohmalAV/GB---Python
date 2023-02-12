# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

def powerRec(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Введите число возводимое в степень: "))
b = int(input("Введите число степени: "))
print(power(a, b))
print(powerRec(a, b))



