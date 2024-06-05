import math

with open("data.txt", 'r', encoding='utf-8') as f:
    arr = f.readlines()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
p = 1.6075
print(f'a = {a}', f'b = {b}', f'c = {c}', sep='\n')
print('Объём эллипсоида:', "{:.3f}".format(4 / 3 * math.pi * a * b * c))
print('Площадь поверхности эллипсоида:',
      "{:.3f}".format(((a ** p * b ** p + b ** p * c ** p + c ** p * a ** p) / 3) ** (1 / p) * 4 * math.pi))
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
