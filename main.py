# 1

'''n = int(int(input()) ** 0.5) + 1
c = 1
for i in range(1, n):
    c += 1
    print(i ** 2)
print(c)'''

# 2

'''a = int(input())
sum1 = 0
c = 2
while a != 0:
    sum1 += a
    a = int(input())
    c += 3
print(sum1)
print(f'Количество операций: {c}')'''

# 3

'''max1 = 1
max2 = 0
n = int(input())
c = 3
while n != 0:
    if n >= max1:
        max2, max1 = max1, n
        c += 1
    elif n >= max2:
        max2 = n
        c += 2
    n = int(input())
    c += 3
print(max2)
print(f'Количество операций: {c + 1}')'''

# 4

'''max1, max2, last, n = 0, 1, int(input()), int(input())
c = 4
while n != 0:
    if last == n:
        max2 += 1
        c += 1
    elif max2 > max1:
        max1, max2 = max2, 1
        c += 3
    else:
        max2 = 1
        c += 1
    last, n = n, int(input())
    c += 4
if max2 > max1:
    max1 = max2
    c += 1
c += 1
print(max1)
print(f'Количество операций: {c + 1}')'''


# 5

'''n = int(input())
arr = []
ind = []
c = 3
while n != 0:
    arr.append(n)
    n = int(input())
    c += 3
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        ind.append(i)
        c += 1
    c += 3
arr.clear()
c += 2
for i in range(len(ind) - 1):
    arr.append(abs(ind[i] - ind[i + 1]))
    c += 3
if arr:
    print(min(arr))
    c += 1
else:
    print(0)
c += 2

print(f'Количество операций: {c + 1}')'''

# 6

'''n = int(input('Введите длину: '))
c = 1
arr = [int(input()) for i in range(n)]
c += n * 2
for i in range(0, n - 1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    c += 3
print(arr)

print(f'Количество операций: {c}')'''

# 7

'''n = int(input('Введите длину: '))
arr = [int(input())]
for i in range(n - 1):
    a = int(input())
    if a < arr[i]:
        print('Вы ввели число меньше предыдущего')
        while True:
            b = int(input(f'Введите число больше или равно {arr[i]}: '))
            if b >= arr[i]:
                arr.append(b)
                break
    else:
        arr.append(a)
print(arr)
kol = 1
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        kol += 1
print(kol)'''

# 8

'''n = int(input('Введите длину: '))
c = 1
arr = [int(input()) for i in range(n)]
c += n * 2
for i in range(n):
    if arr[i] not in arr[i + 1:] and arr[i] not in arr[:i]:
        print(arr[i])
    c += 3
print(arr)

print(c)'''