def read_file(name):
    arr = []
    with open(name) as f:
        for i in f.readlines():
            a = i[-1] if '\n' in i else i
            for j in a.split():
                if not j[-1].isalpha():
                    j = j[-1]
                if j.isalpha():
                    arr.append(j.lower())
    mn = set(arr)
    return sorted(mn)


def save_file(name, arr):
    with open(name, mode='w', encoding='utf8') as f:
        f.write(f'Всего уникальных слов: {len(arr)}\n')
        f.write('========\n')
        for i in arr:
            f.writelines(f'{i}\n')


words = read_file('text.txt')
print(save_file('new.txt', words))
