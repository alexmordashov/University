class System:
    def __init__(self, num, sys):
        self.num = num
        self.sys = sys


    def int_from_10_to_n(self, ans='', abc = "0123456789ABCDEF"):
        num1 = int(self.num)
        if self.num == 0:
            return 0
        while self.num > 0:
            ans += abc[self.num % self.sys]
            self.num //= self.sys
        ans = ans[::-1]
        return ans


    def int_from_n_to_10(self, ans=0, abc = "0123456789ABCDEF"):
        num1 = str(self.num)[::-1]
        for i in range(len(num1)):
            ans += ((self.sys ** i) * (abc.index(num1[len(num1) - 1 - i])))
        return ans
a = System('1321ABC', 10)
print(a.from_n_to_10())
