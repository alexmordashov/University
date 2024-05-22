'''class System:
    def __init__(self, num, sys):
        self.num = num
        self.sys = sys

    def int_from_10_to_n(self, ans='', abc="0123456789ABCDEF"):
        num1 = int(self.num)
        if self.num == 0:
            return 0
        while self.num > 0:
            ans += abc[self.num % self.sys]
            self.num //= self.sys
        ans = ans[::-1]
        return ans

    def int_from_n_to_10(self, ans=0, abc="0123456789ABCDEF"):
        num1 = str(self.num)[::-1]
        for i in range(len(num1)):
            ans += ((self.sys ** i) * (abc.index(num1[len(num1) - 1 - i])))
        return ans

    def float_from_10_to_n(self, ans=''):
        int_part = int(str(self.num).split('.')[0])
        float_part = float(f'0.{str(self.num).split(".")[1]}')
        int_part_trans = self.int_from_10_to_n(int_part)

        # Перевод дробной части в другую систему
        float_part_trans = ''
        precision = len(str(self.num).split(".")[1])
        while float_part > 0 and precision > 0:
            float_part *= self.sys
            float_part_trans += str(int(float_part))
            float_part -= int(float_part)
            precision -= 1
        if int_part_trans == '':
            int_part_trans = '0'
        if float_part_trans == '':
            return int_part_trans
        else:
            return f'{int_part_trans}.{float_part_trans}'


a = System('1488', 16)
print(a.int_from_10_to_n())
print(a.)
'''


class Program:
    def int_from_n_to_10(self, num, sys, ans=0, abc="0123456789ABCDEF"):
        num1 = num[::-1]
        for i in range(len(num1)):
            ans += ((sys ** i) * (abc.index(num[len(num1) - 1 - i])))
        return ans

    def int_from_10_to_n(self, num, sys, ans='', abc="0123456789ABCDEF"):
        if num == 0:
            return 0
        while num > 0:
            ans += abc[num % sys]
            num //= sys
        ans = ans[::-1]
        return ans

    def float_from_10_to_n(self, num, sys, precision=3):
        # Переводим целую часть числа
        int_part = int(num)
        new_int = ''
        if int_part == 0:
            new_int = '0'
        else:
            while int_part > 0:
                new_int = str(int_part % sys) + new_int
                int_part //= sys
        # Переводим дробную часть числа
        float_part = num - int(num)
        new_float = ''
        while precision > 0 and float_part > 0:
            float_part *= sys
            digit = int(float_part)
            new_float += str(digit)
            float_part -= digit
            precision -= 1
        # Собираем полное троичное представление
        if new_float:
            return f"{new_int}.{new_float}"
        else:
            return new_int

    def test1(self):
        print(f"1488 в 10-ой = {self.int_from_10_to_n(1488, 2)} в 2-ой")
        print(f"1488 в 10-ой = {self.int_from_10_to_n(1488, 16)} в 16-ой")
        print(f"1488 в 10-ой = {self.int_from_10_to_n(1488, 8)} в 8-ой")

    def test2(self):
        print(f"B5A2 в 16-ой = {self.int_from_n_to_10('B', 16)} * 16^3 + {self.int_from_n_to_10('5', 16)} * 16^2 + {self.int_from_n_to_10('A', 16)} * 16 + 2 * 16^0 в 10-ой")

    def test3(self):
        a = self.int_from_n_to_10('1100', 2)  # 1100 из 2-ой в 10-ую
        b = self.int_from_n_to_10('10', 4)  # 10 из 4-ой в 10-ую
        c = self.int_from_n_to_10('C', 16)  # С из 16-ой в 10-ую
        d = self.int_from_n_to_10('100', 2)  # 100 из 2-ой в 10-ую

    def test4(self):
        print(f"F95D3 в 16-ой = {self.int_from_10_to_n(self.int_from_n_to_10('F95D3', 16), 2)} в 2-ой")

    def test5(self):
        print(f"1 + 9/5 + 7/15 в 10-ой = {self.float_from_10_to_n((1 + 9/5 + 7/15), 3)} в 3-ой")


program = Program()
# program.test1()
# program.test2()
# program.test3()
# program.test4()
# program.test5()
