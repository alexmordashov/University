class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def turn_on_car(self):
        return 'Автомобиль заведён'

    def turn_off_car(self):
        return 'Автомобиль заглушен'

    def type_of_car(self, type):
        self.type = type
        return self.type

    def year_of_car(self, year):
        self.year = year
        return self.year

    def color_of_car(self, color):
        self.color = color
        return self.color


Turbo = Car('Red', 'Грузовая', '2005')
print('Цвет:', Turbo.color)
print('Тип:', Turbo.type)
print('Год выпуска:', Turbo.year)

Turbo.type_of_car('Легковая')
print('Тип:', Turbo.type)
Turbo.color_of_car('Black')
print('Цвет:', Turbo.color)
Turbo.year_of_car('1999')
print('Год выпуска:', Turbo.year)
print(Car.turn_on_car(Turbo))
print(Car.turn_off_car(Turbo))