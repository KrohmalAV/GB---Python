# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
#  a0 = 0, a1= 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def numFibinachi(num):
    if num in [0, 1]:
        return 1
    return numFibinachi(num-2) + numFibinachi(num - 1)

num = int(input("Введите искомое число Фибоначчи: "))
print(numFibinachi(num))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# num = int(input('Введите число: '))
# list_1 = [0]
# for i in range(1, num + 2):
#     list_1.append(fib(i))
# print(list_1)
# print(f'{num}-е число Фибоначчи =', list_1[-1])
