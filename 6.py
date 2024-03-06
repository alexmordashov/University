def dec2bin(num, ans=''):
    if num == 0:
        return 0
    while num:
        ans += str(num % 2)
        num = num // 2
    ans = ans[::-1]
    return ans


def dec2oct(num, ans=''):
    if num == 0:
        return 0
    while num:
        ans += str(num % 8)
        num = num // 8
    ans = ans[::-1]
    return ans


def dec2hex(num, ans=''):
    abc = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num == 0:
        return 0
    while num:
        if num % 16 >= 10 and num % 16 < 16:
            ans += abc[num % 16]
        else:
            ans += str(num % 16)
        num = num // 16
    ans = ans[::-1]
    return ans


print(dec2hex(256546))

