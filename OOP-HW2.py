# MIN 545 OOP with Python HW2
# This code belongs to Nurdan Emin
# HW2: Develop an inheritance hierarchy based upon the following Polygon class.

import math


class Polygon:
    def __init__(self, sides: list or tuple):
        """Initialized with the lengths of the sides"""
        for s in sides:
            if s <= 0:
                raise ValueError('Side lengths must be positive')

        self._sides = sides
        self._name = "Polygon"

    def name(self):
        return self._name

    def area(self):
        """The area of an arbitrary polygon is unknown"""
        return math.nan  # placeholder

    def perimeter(self):  # same for all subclasses of Polygon class
        total = 0.0
        for s in self._sides:
            total += s
        return total


# TODO : 1  implement classes Triangle and Parallelogram that extend this base class

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):  # takes 3 side lenghts to initialize and initialize polygon class by giving them as tuple
        super().__init__(
            (side1, side2, side3))  # takes the side lengths and then initializes them to Polygon class  as tuple
        self._name = "Triangle"

    # we only need to define area method for each subclass of Polygon class because
    # side lengths are given as tuple to polygon class and perimeter definition is same for all polygons
    # Also in this way we don't need to write a code to check value of each side lengths for each subclass.

    def area(self):
        """" Returns area of a triangle with known side lengths"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2]))


class Parallelogram(Polygon):
    def __init__(self, side1, side2, side3, side4):  # takes 4 side lenghts to initialize
        super().__init__((side1, side2, side3, side4))
        self._name = "Parallelogram"


# Since there is not a common formula for area of parallelograms(if only side lengths are known)
# I did not define an area method for parallelograms.

# TODO 2 :implement IsoscelesTriangle, EquilateralTriangle,Rectangle, and Square classes


class IsocelesTriangle(Triangle):
    def __init__(self, equal_sides, side3):
        """Initializes first with  the equal sides and the other side"""
        super().__init__(equal_sides, equal_sides, side3)
        self._name = "IsoscelesTriangle"


class EquilateralTriangle(Triangle):
    def __init__(self, side):     # takes only 1 side length
        super().__init__(side, side, side)
        self._name = "EquilateralTriangle"


class Rectangle(Parallelogram):
    def __init__(self, side1, side2):
        super().__init__(side1, side1, side2, side2)
        self._name = "Rectangle"

    def area(self):
        return self._sides[1] * self._sides[3]


class Square(Parallelogram):
    def __init__(self, side):
        super().__init__(side, side, side, side)
        self._name = "Square"

    def area(self):
        return self._sides[0] * self._sides[0]


# TODO 3 :test the cases

"""shapelist = [Polygon([1.0, 4.5, 3.1, 3.3]),
             Triangle(3.4, 5.3, 4.2),
             IsocelesTriangle(4.1, 1),
             EquilateralTriangle(4.2),
             Rectangle(5, 4),
             Square(3.25)]
for shape in shapelist:
    print('{0} Area: {1:.3f}  Perimeter: {2:.3f}'.format(shape.name(),
                                                         shape.area(),
                                                         shape.perimeter()))"""
