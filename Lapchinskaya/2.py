import random
import math

alpha = 2 * math.pi * random.random()
print(alpha)
print('z1 =', "{:.2f}".format((math.cos(alpha) + math.sin(alpha)) / (math.cos(alpha) - math.sin(alpha))))
print('z2 =', "{:.2f}".format(math.tan(2 * alpha) + 1 / math.cos(2 * alpha)))

