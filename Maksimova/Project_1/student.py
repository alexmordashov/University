class Student:
    def __init__(self, health, money, mood, iq, energy, rating, date):
        self.health = health
        self.money = money
        self.mood = mood
        self.iq = iq
        self.energy = energy
        self.rating = rating
        self.date = date

    def __str__(self):
        return f"Здоровье: {self.health}\nНастроение: {self.mood}\nИнтеллект: {self.iq}\nРейтинг в университете:{self.rating}\nЭнергия: {self.energy}\nДеньги: {self.money}"

    def next_day(self):
        # изменить текстовый файл(энергия +100, здоровье -10), рейтинг в университете +(0 или -10 если не посетил занятия))
        self.health -= 100
        self.energy = 100
        #self.rating = ?
        #self.mood = ?
        self.date += 1
        with open("data.txt", 'w+') as f:
            f.write('\n'.join())
        pass

    def food(self):
        with open('food.txt', encoding='utf-8') as f:
            for i in f.readlines():
                print(i[:-1])
        otvet = input('Что будем делать?')

    def work(self):
        with open('work.txt', encoding='utf-8') as f:
            for i in f.readlines():
                print(i[:-1])

    def entertainment(self):
        with open('entertainment.txt.txt', encoding='utf-8') as f:
            for i in f.readlines():
                print(i[:-1])

    def study(self):
        with open('study.txt', encoding='utf-8') as f:
            for i in f.readlines():
                print(i[:-1])

    '''def clear_level(self):
        f = open('test.txt', 'w+')
        f.seek(0)
        f.close()

    def read_level(self):
        with open("data.txt") as f:
            arr = f.read().splitlines()
        return arr

    def write_level(self, arr):
        with open("data.txt", 'w+') as f:
            f.write('\n'.join(arr))'''
