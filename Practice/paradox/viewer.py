from Practice.paradox.paradox import birthday, monty_hall


def show():
    while True:
        a = input('1. Запуск Monty_Hall\n2. Запуск Birthday\n3. Выход\n')
        if a == '1':
            try:
                print((monty_hall(int(input('Введите кол-во экспериментов:')))))
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(10000)')
                print(monty_hall(10000))
        if a == '2':
            print('Введите кол-во чел. в 1 группе, кол-во чел. в 2 группе, кол-во экспериментов:')
            try:
                kol1 = int(input())
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(23)')
                kol1 = 23
            try:
                kol2 = int(input())
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(60)')
                kol2 = 60
            try:
                kol3 = int(input())
            except ValueError:
                print('Неправильный формат ввода, использовано значение по умолчанию(1000)')
                kol3 = 1000
            print(birthday(kol1, kol2, kol3))
        if a == '3':
            break