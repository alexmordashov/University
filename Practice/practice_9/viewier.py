from program import *


def show():
    while True:
        print()
        print('0. Сменить рабочий каталог\n1. Преобразовать PDF в Docx\n'
              '2. Преобразовать Docx в PDF\n3. Произвести сжатие изображений\n4. Удалить группу файлов\n5. Выход\n')
        choose = input('Выберите действие: ')
        print()
        if choose == '0':
            catalog = input('Введите абсолютный путь каталога: ')
            print(f"Текущий каталог: {change_catalog(catalog)}")
        elif choose == '1':
            chosen1()
        elif choose == '2':
            chosen2()
        elif choose == '3':
            chosen3()
        elif choose == '4':
            chosen4()
        elif choose == '5':
            break
        else:
            print('Вы ошиблись, введите номер команды ещё раз')


if __name__ == "__main__":
    show()
