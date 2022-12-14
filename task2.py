# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ W) для всех значений предикат.
# _________________________________________________________
print('X Y Z W')
for x in range(2):
    for Y in range(2):
        for Z in range(2):
            for W in range(2):
                if not (W and Z) or not Y or (not x == W):
                    print(x, Y, Z, W)
