import random
arr = []
mas = [[random.randrange(-20, 21) for j in range(8)] for i in range(8)]
maxel = -100
for i in range(len(mas)):
    for j in range(len(mas)):
        if mas[i][j] > maxel:
            maxel = mas[i][j]
print(maxel)
for i in range(len(mas)):
    for j in range(len(mas)):
        if i == j:
            arr.append(maxel)
