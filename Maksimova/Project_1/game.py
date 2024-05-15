'''from student import Student
import os

'''def game():
    while True:
        with open("data.txt") as f:
            arr = f.read().splitlines()
        student = Student(arr[0], arr[1], arr[2], arr[3], arr[4])
        print(student)
        otvet = input('Что вы хотите сделать?\n1 - Поработать\n2 - Развлечься\n3 - Поесть\n4 - Выйти\n')
        if otvet == "1":
            pass
        elif otvet == "2":
            pass
        elif otvet == "3":
            pass
        else:
            break
        print(student)'''


def clear_level():
    f = open('test.txt', 'w+')
    f.seek(0)
    f.close()


def read_level():
    with open("data.txt") as f:
        arr = f.read().splitlines()
    return arr


def write_level(arr):
    with open("data.txt", 'w+') as f:
        f.write('\n'.join(arr))


def game():
    arr = ['100', '1000', '100', '0', '100', '100']
    while True:
        otvet = input('Что вы хотите сделать?\n1 - Начать новую игру\n2 - Продолжить игру\n3 - Выйти')
        if otvet == '1':
            write_level(arr)
            student = Student(arr[0], arr[1], arr[2], arr[3], arr[4])
            game1(student)
        if otvet == '2':
            if os.stat("data.txt").st_size == 0:
                print('У вас нет начатой игры. Начнем новую игру!')
                write_level(arr)
                student = Student(arr[0], arr[1], arr[2], arr[3], arr[4])
            else:
                arr = read_level()
                student = Student(arr[0], arr[1], arr[2], arr[3], arr[4])
            game1(student)
            break
        else:
            break


def game1(student):
    while True:
        print(student)  # выводим характеристики студента и дату
        otvet = input('Что будем делать?\n1 - Работать\n2 - Есть\n3 - Кайфовать\n4 - Учиться\n5 - Начать следующий день\n6 - Выйти из игры')
        if otvet == '1':
            student.work()
        if otvet == '2':
            student.food()
        if otvet == 'Кайфовать':
            student.entertainment()
        if otvet == '4':
            student.study()
        if otvet == '5':
            student.next_day()
        if otvet == '6':
            break
        if 'рейтинг в университете' == 0:
            print('вас исключили, вы проиграли')
            clear_level()
            break
        if 'здоровье' == 0:
            print('вы умерли')
            clear_level()
            break
        if 'настроение' == 0:
            print('вы впали в депрессию')
            clear_level()
        if 'энергия' == 0:
            print('вы устали')
            student.next_day()'''

from student import Student
import os

'''def game():
    while True:
        with open("data.txt") as f:
            arr = f.read().splitlines()
        student = Student(arr[0], arr[1], arr[2], arr[3], arr[4])
        print(student)
        otvet = input('Что вы хотите сделать?\n1 - Поработать\n2 - Развлечься\n3 - Поесть\n4 - Выйти\n')
        if otvet == "1":
            pass
        elif otvet == "2":
            pass
        elif otvet == "3":
            pass
        else:
            break
        print(student)'''


def clear_level():
    f = open('test.txt', 'w+')
    f.seek(0)
    f.close()


def read_level():
    with open("data.txt") as f:
        arr = f.read().splitlines()
    return arr


def write_level(arr):
    with open("data.txt", 'w+') as f:
        f.write('\n'.join(arr))


def game():
    arr = ['100', '1000', '100', '0', '100', '100', '1']
    while True:
        otvet = input('Что вы хотите сделать?\n1 - Начать новую игру\n2 - Продолжить игру\n3 - Выйти')
        if otvet == '1':
            write_level(arr)
            student = Student(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
            game1(student)
        if otvet == '2':
            if os.stat("data.txt").st_size == 0:
                print('У вас нет начатой игры. Начнем новую игру!')
                write_level(arr)
                student = Student(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
            else:
                arr = read_level()
                student = Student(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
            game1(student)
            break
        else:
            break


def game1(student):
    while True:
        print(student)  # выводим характеристики студента и дату
        otvet = input('Что будем делать?\n1 - Работать\n2 - Есть\n3 - Кайфовать\n4 - Учиться\n5 - Начать следующий день\n6 - Выйти из игры')
        if otvet == '1':
            student.work()
        if otvet == '2':
            student.food()
        if otvet == '3':
            student.entertainment()
        if otvet == '4':
            student.study()
        if otvet == '5':
            student.next_day()
        if otvet == '6':
            break
        if student.rating == 0:
            print('вас исключили, вы проиграли')
            clear_level()
            break
        if student.health == 0:
            print('вы умерли')
            clear_level()
            break
        if student.mood == 0:
            print('вы впали в депрессию')
            clear_level()
        if student.energy == 0:
            print('вы устали')
            student.next_day()

