"""
Напишите программу, которая принимает на вход координаты
точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

x = float(input("Введите значение Х координаты точки: "))
y = float(input("Введите значение Y координаты точки: "))
if x > 0 and y > 0:
    print("Указанная точка лежит в I четверти координатной плоскости")
elif x < 0 and y > 0:
    print("Указанная точка лежит в II четверти координатной плоскости")
elif x < 0 and y < 0:
    print("Указанная точка лежит в III четверти координатной плоскости")
elif x > 0 and y < 0:
    print("Указанная точка лежит в IV четверти координатной плоскости")
elif x == 0 and y > 0:
    print("Указанная точка лежит на оси Y между I и II четвертями координатной плоскости")
elif x == 0 and y < 0:
    print("Указанная точка лежит на оси Y между III и IV четвертями координатной плоскости")
elif x > 0 and y == 0:
    print("Указанная точка лежит на оси X между I и IV четвертями координатной плоскости")
elif x < 0 and y == 0:
    print("Указанная точка лежит на оси X между II и III четвертями координатной плоскости")
else:
    print("Указанная точка является центром координатной плоскости")