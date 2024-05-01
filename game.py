# Файл Game
def clear_file():
    f = open('test.txt', 'w+')
    f.seek(0)
    f.close()

def game():
    while True:
        otvet = input('Что вы хотите сделать?')
        if otvet == 'Начать новую игру':
            clear_file
            student = new Student('параметры')
            game1(student)
        if otvet == 'Продолжить игру':
            f = open('test.txt', 'r')
            if f.isempty():
                print('У вас нет начатых игр')
                student = new Student('параметры')
            else:
                student = new Student('параметры из текстового файла')
            game1(student)
            break
        else:
            break
def game1():
    while True:
        print(student) # выводим характеристики студента и дату
        otvet = input('Что будем делать?')
        if otvet == 'Работать':
            student.work()
        if otvet == 'Есть':
            student.food()
        if otvet == 'Кайфовать':
            student.entertainment()
        if otvet == 'Учиться':
            student.study()
        if otvet == 'Начать следующий день':
            student.next_day()
        if otvet == 'Выйти из игры':
            break
        if 'рейтинг в университете' == 0:
            print('вас исключили, вы проиграли')
            clear_file()
            break
        if 'здоровье' == 0:
            print('вы умерли')
            clear_file()
            break
        if 'настроение' == 0:
            print('вы впали в депрессию')
            clear_file()
        if 'энергия' == 0:
            print('вы устали')
            student.next_day()
            
# Файл Student
def next_day():
    # изменить текстовый файл(энергия +100, здоровье -10), рейтинг в университете +(0 или -10 если не посетил занятия))
    continue
def food():
    # выводим возможную еду из файла csv
    # считываем выбор игрока и применяем его
def work():
    # выводим возможную раюоту из файла csv
    # считываем выбор игрока и применяем его
def entertainment():
    # выводим возможные развлечения из файла csv
    # считываем выбор игрока и применяем его