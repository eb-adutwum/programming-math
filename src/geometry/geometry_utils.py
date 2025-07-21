import math

class _Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def _area(self):
        """
        Calculate the area of the rectangle.
         :return: Area of the rectangle.
        """
        return self.l * self.b

    def _perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        :return: Perimeter of the rectangle.
        """
        return 2 * self.l + 2 * self.b


class _Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _area(self):
        """Calculate the area of the triangle using Heron's formula.
        :return: Area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        cos_C = (self.a**2 + self.b**2 - self.c**2) / (2 * a * b)
        angle_C = math.acos(cos_C)
        return 0.5 * self.a * self.b * math.sin(angle_C)

    def _perimeter(self):
        """Calculate the perimeter of the triangle.
        :return: Perimeter of the triangle.
        """
        return self.a + self.b + self.c


class _Circle:
    def __init__(self, r):
        self.r = r

    def _area(self):
        """
        Calculate the area of the circle.
        :return: Area of the circle.
        """
        return math.pi * self.r**2

    def _circumference(self):
        """
        Calculate the circumference of the circle.
        :return: Circumference of the circle.
        """
        return 2 * math.pi * self.r
