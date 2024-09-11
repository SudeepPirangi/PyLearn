"""
Demonstrates some basics of Python OOPS
"""

from math import sqrt

# 1. Write a class "Line" with methods to find "distance" and "slope" given 2 coordinates.
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)

print("\nLine class")

class Line():
    """Geometric Line"""

    def __init__(self, co1, co2):
        self.co1 = co1
        self.co2 = co2

    def distance(self):
        """Returns distance between given coords"""
        x1, y1 = self.co1
        x2, y2 = self.co2

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        """Return slope of the coords"""
        x1, y1 = self.co1
        x2, y2 = self.co2

        return (y2 - y1)/(x2 - x1)

line = Line((3, 2), (8, 10))

print(f"Distance between coordinates is {line.distance():2.2f}")
print(f"Slope of coordinates is {line.slope():2.2f}")


# 2. Create a Cylinder class that calculates the "volume" and "surface_area" of a cylinder
# Given height = 2, radius = 3

print("\nCylinder class")

class Cylinder():
    """Geometric Cylinder"""

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def surface_area(self):
        """Returns surface area of the cylinder [2 * pi * r * (r + h)]"""
        return 2 * 3.14 * self.radius * (self.radius + self.height)

    def volume(self):
        """Returns the volume of a cylinder [pi * (r ** 2) * h]"""
        return 3.14 * (self.radius ** 2) * self.height

cylinder = Cylinder(2, 3)

print(f"Volume of the Cylinder is {cylinder.volume():2.2f}")
print(f"Surface Area of the Cylinder is {cylinder.surface_area():2.2f}")
