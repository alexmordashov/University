class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Длины сторон треугольника: {self.a}, {self.b}, {self.c}'

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def height(self):
        s = self.square()
        return f'{2 * s / self.a}, {2 * s / self.b}, {2 * s / self.c}'

    def is_triangle_exist(self):
        if self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b:
            return ('Треугольник существует', 1)
        else:
            return ('Треугольник не существует', 0)

    is_triangle = property(is_triangle_exist)


triangle = Triangle(56, 76, 78)
print(triangle)
print(triangle.is_triangle[0])
if triangle.is_triangle[1]:
    print(f'Периметр треугольника: {triangle.perimetr()}')
    print(f'Площадь треугольника: {triangle.square()}')
    print(f'Высоты треугольника: {triangle.height()}')
print('=====')
print('Артём Беспечалов 2023-ФГиИБ-ПИ-1б')
