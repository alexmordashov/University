import json
import datetime


class Student:
    def __init__(self, arr):
        self.health = arr[0]
        self.mood = arr[1]
        self.energy = arr[2]
        self.iq = arr[3]
        self.rating = arr[4]
        self.money = arr[5]
        self.date = datetime.datetime.strptime(arr[6], "%Y-%m-%d")
        self.is_job = 0
        self.date_start_job = datetime.datetime.strptime("1970-01-01", "%Y-%m-%d")
        self.month_from_start_job = 0
        self.salary = 0

    def next_day(self):
        # изменить текстовый файл(энергия +100, здоровье -10), рейтинг в университете +(0 или -10 если не посетил занятия))
        if self.is_job:
            if (
                    self.date.year - self.date_start_job.year) * 12 + self.date.month - self.date_start_job.month > self.month_from_start_job and self.date.day + 1 == self.date_start_job.day:
                self.money = str(int(self.money) + self.salary)
                self.month_from_start_job += 1
                #print(self.date, self.date_start_job)
        if float(self.health) - 0.2 <= 0:
            print('Вы умерли')
            with open('specifications.json', 'w') as f:
                pass
            return 1
        elif float(self.mood) - 0.2 <= 0:
            print('Вы впали в депрессию')
            with open('specifications.json', 'w') as f:
                pass
            return 1
        elif float(self.rating) - 0.6 <= 0:
            print('Вас отчислили')
            with open('specifications.json', 'w') as f:
                pass
            return 1
        else:
            self.health = str(float(self.health) - 0.2)
            self.mood = str(float(self.mood) - 0.2)
            self.rating = str(float(self.rating) - 0.6)
            self.energy = '100'
            # self.rating = ?
            # self.mood = ?
            self.date += datetime.timedelta(days=1)
            return 0

    def food(self):
        pass

    def job(self):
        if self.is_job:
            pass

    def entertainment(self):
        pass

    def study(self):
        pass

    def communication(self):
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
