import math
import random

a, b, c = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
p = 1.6075
print(f'a = {a}', f'b = {b}', f'c = {c}', sep='\n')
print('Объём эллипсоида:', "{:.3f}".format(4 / 3 * math.pi * a * b * c))
print('Площадь поверхности эллипсоида:',
      "{:.3f}".format(((a ** p * b ** p + b ** p * c ** p + c ** p * a ** p) / 3) ** (1 / p) * 4 * math.pi))

