"""
Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
count = 0
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            res1 = not(x or y or z)
            res2 = not(x) and not(y) and not(z)
            print(f"При X = {bool(x)} Y = {bool(y)} и Z = {bool(y)} истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z)  => {res1==res2}") 
            if res1 == res2:
                count += 1
if count == 2**3:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) истинно при любых значениях предикат.")
else:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) не для всех значений предикат является истинным.")