import pymorphy3
import pymorphy3_dicts_ru
import translate
from translate import Translator
import csv


def get_w():
    with open('input.txt', mode="r", encoding="utf8") as f:
        str1 = f.read().splitlines()
    str_list = [str1[i].split(' ') for i in range(len(str1))]
    clear = []
    for i in range(len(str_list)):
        for j in str_list[i]:
            j = ''.join(filter(str.isalpha, j)).lower()
            if len(j) > 0:
                clear.append(j)
    return clear


def normal_w(clear):
    return [pymorphy3.MorphAnalyzer().parse(i)[0].normal_form for i in clear]


def make_dict(normal_l):
    d = {}
    for i in range(len(normal_l)):
        if not normal_l[i] in d:
            d[normal_l[i]] = 1
        else:
            d[normal_l[i]] += 1
    return d


def sort_list(d):
    return sorted(d.items(), key=lambda i: i[1], reverse=True)


def translate_l(sort_l):
    return [[sort_l[i][0], Translator(from_lang='ru', to_lang="en").translate(str(sort_l[i][0])).lower(), sort_l[i][1]]
            for i in range(len(sort_l))]
