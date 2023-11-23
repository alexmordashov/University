def prog():
    while True:
        if input('Запуск - 1\nВыход - 0\n') == '1':
            try:
                file = input('Введите имя файла: ')
                with open(f'{file}.txt') as f:
                    n = int(f.readline())
                    arr = [int(i) for i in f.readlines()]
                print(arr)
            except FileNotFoundError:
                print('Такого файла нет\n')
                return prog()
            except ValueError:
                print('В файле обнаружена буква\n')
                return prog()
        else:
            break