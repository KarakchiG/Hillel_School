from abc import ABC, abstractmethod
import math

pi = math.pi


class Figure(ABC):



    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_square(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def __str__(self):
        return f"Triangle (side a = {self.side_a}, side b = {self.side_b}, side c = {self.side_c})"


class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_square(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"Round (radius = {self.radius})"


triangle1 = Triangle(2, 3, 4)
triangle2 = Triangle(7, 8, 9)

round1 = Round(5)
round2 = Round(10)

collection_of_figures = [triangle1, triangle2, round1, round2]

for figure in collection_of_figures:
    print(f"Figure: {figure}")
    print("Perimeter:", figure.get_perimeter(), "cm")
    print("Square:", figure.get_square(), "cm^2")
