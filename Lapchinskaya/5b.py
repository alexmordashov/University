import math


def func(x0, xn, hx):
    kol = 0
    if '.' in hx:
        kol = len(hx.split('.')[1])
    for x in [i / 10**kol for i in range(int(x0 * 10**kol), int((xn + float(hx)) * 10**kol), int(float(hx) * 10**kol))]:
        if x <= -3 or x >= 6:
            print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(3)}')
        elif x > -3 and x < 0:
            print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(-1 * x)}')
        elif x >= 0 and x < 6:
            print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(x * 0.5)}')


func(-10, 20, '0.05')
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
