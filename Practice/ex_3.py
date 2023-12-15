class SuperStr(str):
    def __init__(self, stroka):
        self.stroka = stroka

    def is_repeatance(self, s):
        if isinstance(s, str) == False:
            return False
        elif len([x for x in self.stroka.split(s) if len(x) > 0]) == 0:
            return True
        else:
            return False

    def is_palindrom(self):
        if self.stroka == self.stroka[::-1]:
            return True
        else:
            return False


s = SuperStr("123123123123")
print(s.is_repeatance("123"))  # True
print(s.is_repeatance("123123"))  # True
print(s.is_repeatance("123123123123"))  # True
print(s.is_repeatance("12312"))  # False
print(s.is_repeatance(123))  # False
print(s.is_palindrom())  # False
print(s * 2)  # 123123123123 (строка)
print(int(s) * 2)  # 123123123123 (целое число)
print(s + "qwe")  # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom())