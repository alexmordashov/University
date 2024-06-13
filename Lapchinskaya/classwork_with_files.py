import math

with open("data.txt", 'r', encoding='utf-8') as f:
    arr = f.readlines()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
p = 1.6075
f.close()
with open("new_data.txt", 'w', encoding='utf-8') as f:
    f.write(str("{:.3f}".format(4 / 3 * math.pi * a * b * c)) + '\n')
    f.write(str("{:.3f}".format(((a ** p * b ** p + b ** p * c ** p + c ** p * a ** p) / 3) ** (1 / p) * 4 * math.pi)))
f.close()
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
