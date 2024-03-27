import random

def sum_mas(arr):
    sum1 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
    return sum1

def maxel(arr):
    maxel = -100
    for i in range(len(arr)):
        for j in range(len(arr)):
            if int(arr[i][j]) > maxel:
                maxel = int(arr[i][j])
    return maxel

def print_mas(arr):
    for i in arr:
        print(' '.join(i))

def work():
    diag_A = []
    A = [[str(random.randrange(-20, 21)) for j in range(8)] for i in range(8)]
    print('Массив A:')
    print_mas(A)
    maxel_A = maxel(A)
    print('=====')
    print(f'Макс. элемент A: {maxel_A}')
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                diag_A.append(int(A[i][j]))
    sum_diag_A = sum_mas(diag_A)
    print(f'Сумма элементов главной диагонали A: {sum_diag_A}')
    print(f'Среднее значение главной диагонали A: {sum_diag_A / len(diag_A)}')
    B = [[str(int(maxel_A) - sum_mas(diag_A) / len(diag_A)) for j in range(8)] for i in range(8)]
    print('=====')
    print('Массив B:')
    print_mas(B)
    print('=====')
    print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')

work()
