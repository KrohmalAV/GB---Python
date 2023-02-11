# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def replacement(array):
    resMax = max(array)
    resMin = min(array)
    for i in range(len(array)):
        if array[i] == resMax:
            array[i] = resMin
    return array   

res = [1, 3, 3, 4, 5]
print(res)
print(replacement(res))
    