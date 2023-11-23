import random
import gen

def game():
    word_list = gen.get_words()
    record = 0
    skill = 0
    difficult = input('Уровень сложности:\n сложный - введите "3"'
                      '\n средний - введите "2"'
                      '\n легкий - введите "1"\n')
    if difficult.strip() == '3':
        skill = 3
    elif difficult.strip() == '2':
        skill = 5
    elif difficult.strip() == '1':
        skill = 7
    while True:
        word = word_list.pop(random.randrange(len(word_list)))
        zagadano = ["■"] * len(word)

        while True:
            print(''.join(zagadano), word)
            otvet = input('Введите букву или слово целиком: ').strip()

            if otvet.upper() in word and len(otvet) == 1:
                for i in range(len(word)):
                    if word[i] == otvet.upper():
                        zagadano[i] = otvet.upper()
                print(f"Откройте букву: '{otvet.upper()}'")

            elif not otvet.upper() in word:
                skill -= 1
                print(f"Такой буквы нет в слове(. Вы теряете жизнь.")

            if len(otvet) > 1 and otvet.upper() == word or ''.join(zagadano) == word:
                print(f"Вы угадали слово '{word.upper()}'! Вы выиграли!")
                record += 1
                break

            elif otvet.upper() != word and len(otvet) > 1:
                skill -= skill + 1
                print(f'Вы записали слово неправильно, поэтому выбываете из игры\nВаш рекорд: {gen.get_records(record)}')
                exit()

            if skill == 0:
                print('')
                print(f"Жизни закончились, вы проиграли(. Загаданное слово было: {word}\nВаш рекорд: {gen.get_records(record)}")
                exit()

        if input('Хотите сыграть ещё раз? (да/нет)\n').lower() == 'нет':
            print(f'Ваш рекорд: {gen.get_records(record)}')
            break
        if len(word_list) == 0:
            print(f'Слова в списке закончились. Вы просто гений этой игры! Ваш рекорд: {gen.get_records(record)}')
            break
