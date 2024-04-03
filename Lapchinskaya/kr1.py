import math

for x in [i / 10 for i in range(20, 52, 2)]:
    print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(3 * x * math.sin(x) ** 2 + math.tan(2 * x))}')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
