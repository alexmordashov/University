for x in [i / 100 for i in range(-1000, 2005, 5)]:
    if x <= -3 or x >= 6:
        print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(3)}')
    elif x > -3 and x < 0:
        print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(-1 * x)}')
    elif x >= 0 and x < 6:
        print(f'x = {"{:.3f}".format(x)} f(x) = {"{:.3f}".format(x * 0.5)}')