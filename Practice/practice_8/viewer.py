from english import *


def show():
    dict = translate_l(sort_list(make_dict(normal_w(get_w()))))
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        wr = csv.writer(file)
        wr.writerow(['Исходное слово', 'Перевод', 'Количество упоминаний'])
        for i in dict:
            wr.writerow(i)
    print('Словарь создан')
