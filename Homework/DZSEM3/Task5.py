# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input("Введите число: "))
listFibonachi = [0 for i in range(2 * num + 1)]
listFibonachi[num + 1] = listFibonachi[num - 1] = 1
for i in range(num+2, 2*num + 1):
    listFibonachi[i] = listFibonachi[i-1] + listFibonachi[i-2]
    listFibonachi[-(i+1)] = ((-1)**(i-1)) * listFibonachi[i]
print(listFibonachi)