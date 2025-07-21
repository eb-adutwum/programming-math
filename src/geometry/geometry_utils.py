"""Geometry module containing classes for geometric shapes."""

import math


class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, l, b):
        if l <= 0 or b <= 0:
            raise ValueError("Sides must be positive numbers.")
        self.l = l
        self.b = b

    def area(self):
        """
        Calculate the area of the rectangle.
         :return: Area of the rectangle.
        """
        return self.l * self.b

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        :return: Perimeter of the rectangle.
        """
        return 2 * self.l + 2 * self.b


class Triangle:
    """Class representing a triangle."""

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive numbers.")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Calculate the area of the triangle using Heron's formula.
        :return: Area of the triangle.
        """

        cos_theta = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)
        theta = math.acos(cos_theta)
        return 0.5 * self.a * self.b * math.sin(theta)

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        :return: Perimeter of the triangle.
        """
        return self.a + self.b + self.c


class Circle:
    """Class representing a circle."""

    def __init__(self, r):
        if r <= 0:
            raise ValueError("Radius must be a positive number.")

        self.r = r

    def area(self):
        """
        Calculate the area of the circle.
        :return: Area of the circle.
        """
        return math.pi * self.r**2

    def circumference(self):
        """
        Calculate the circumference of the circle.
        :return: Circumference of the circle.
        """
        return 2 * math.pi * self.r
