import random


def couples(dates):
    k = 0
    for i in range(len(dates)):
        for j in range(i + 1, len(dates)):
            if dates[i] == dates[j]:
                k += 1
    return k


def birthday(n):
    count23 = 0
    count60 = 0
    for l in range(n):
        dates_23 = [(random.randrange(1, 29), random.randrange(1, 13)) for i in range(23)]
        dates_60 = [(random.randrange(1, 29), random.randrange(1, 13)) for i in range(60)]
        c23 = couples(dates_23)
        c60 = couples(dates_60)
        if c23:
            count23 += 1
        if c60:
            count60 += 1
    return f'Вероятность совпадения в группе из 23 человек: {int(count23 / n * 100)}%\nВероятность совпадения в группе из 60 человек: {int(count60 / n * 100)}%'
