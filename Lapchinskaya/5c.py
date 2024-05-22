import math


class Function:
    def __init__(self, x0, xn, hx):
        self.x0 = x0
        self.xn = xn
        self.hx = str(hx)


    def func(self):
        kol = 0
        if '.' in self.hx:
            kol = len(self.hx.split('.')[1])
        for x in [i / 10**kol for i in range(int(self.x0 * 10**kol),
                                             int((self.xn + float(self.hx)) * 10**kol),
                                             int(float(self.hx) * 10**kol))]:
            if x <= -3 or x >= 6:
                print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(3)}')
            elif x > -3 and x < 0:
                print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(-1 * x)}')
            elif x >= 0 and x < 6:
                print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(x * 0.5)}')


graf = Function(-10, 20, 0.05)
graf.func()
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
