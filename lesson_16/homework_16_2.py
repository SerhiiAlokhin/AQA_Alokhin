from abc import ABC, abstractmethod
import math


# Абстрактний клас "Фігура"
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
            self.__side_a = side_a
            self.__side_b = side_b
            self.__side_c = side_c
    def area(self):
        # Формула Герона или площадь треугольника по его трем сторонам: S = √p · (p — a)(p — b)(p — c)
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

figures = [
    Rectangle(5, 10),
    Triangle(12, 16, 20),
    Circle(9)
]
for figure in figures:
    print(f"Фігура: {figure.__class__.__name__}")
    print(f"Площа: {figure.area()}")
    print(f"Периметр: {figure.perimeter()}")
    print("=" * 20)
