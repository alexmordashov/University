class Student:
    def __init__(self, health, money, mood, iq, energy, rating):
        self.health = health
        self.money = money
        self.mood = mood
        self.iq = iq
        self.energy = energy
        self.rating = rating

    def __str__(self):
        return f"Здоровье: {self.health}\nНастроение: {self.mood}\nИнтеллект: {self.iq}\nРейтинг в университете:{self.rating}\nЭнергия: {self.energy}\nДеньги: {self.money}"

    def next_day(self):
        # изменить текстовый файл(энергия +100, здоровье -10), рейтинг в университете +(0 или -10 если не посетил занятия))
        with open("data.txt", 'w+') as f:
            f.write('\n'.join())
        pass

    def food(self):
        # выводим возможную еду из файла csv
        # считываем выбор игрока и применяем его
        pass

    def work(self):
        # выводим возможную работу из файла csv
        # считываем выбор игрока и применяем его
        pass

    def entertainment(self):
        # выводим возможные развлечения из файла csv
        # считываем выбор игрока и применяем его
        pass

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
