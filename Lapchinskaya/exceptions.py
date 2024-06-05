import os

try:
    with open(input('Введите имя файла: '), 'r') as f:
        print(''.join(f.readlines()))
except FileNotFoundError as e:
    print('Файл не найден')
print("Программу выполнил студент 2023-ФГиИБ-ПИ-1б Беспечалов Артём")
