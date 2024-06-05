try:
    with open(input('Введите имя файла: '), 'r') as f:
        print(''.join(f.readlines()))
except FileNotFoundError as e:
    print('Файл не найден')
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
