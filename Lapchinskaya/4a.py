import random
arr = []
A = [[str(random.randrange(-20, 21)) for j in range(8)] for i in range(8)]

print('Массив A:')
for i in A:
    print(' '.join(i))

maxel = -100
for i in range(len(A)):
    for j in range(len(A)):
        if int(A[i][j]) > maxel:
            maxel = int(A[i][j])
            
print('=====')
print(f'Макс. элемент A: {maxel}')

for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            arr.append(int(A[i][j]))
            
print(f'Сумма элементов главной диагонали A: {sum(arr)}')
print(f'Среднее значение главной диагонали A: {sum(arr)/len(arr)}')

B = [[str(int(maxel) - sum(arr) / len(arr)) for j in range(8)] for i in range(8)]

print('=====')
print('Массив B:')
for i in B:
    print(' '.join(i))
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
