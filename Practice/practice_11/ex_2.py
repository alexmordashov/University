import math


class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_volume(self):
        return (4 / 3) * (math.pi) * (self.r) ** 3

    def get_square(self):
        return 4 * math.pi * ((self.r) ** 2)

    def get_radius(self):
        return float(self.r)

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2 <= (self.r) ** 2:
            return True
        else:
            return False


s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))
print(s0.get_radius())

s0 = Sphere()
print(s0.get_radius())
print(s0.get_center())