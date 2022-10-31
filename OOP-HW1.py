# OOP with Python HW1
# Code belongs to Nurdan Emin


from math import pi, sqrt


class Circle:
    """A class that represent circle, takes value of radius to create instance of class,
     if radius is not given it defaults  to 1."""

    def __init__(self, radius=1):
        if not isinstance(radius, (int, float)):
            raise TypeError('Please provide an integer or float value for the radius of circle!')
        else:
            self._radius = float(radius)
            self._diameter = None
            self._area = None

    def set_radius(self, new_radius):
        self._radius = float(new_radius)

    def get_radius(self):
        return self._radius

    def set_area(self, new_radius):
        self._area = pi * (new_radius ** 2)

    def get_area(self):
        if not self._area:
            self.set_area(self._radius)
        return self._area

    def set_diameter(self, new_radius):
        self._diameter = 2 * new_radius

    def get_diameter(self):
        if not self._diameter:
            self.set_diameter(self._radius)
        return self._diameter

    def radius(self, radius_val=None):
        """if positional argument is not provided it returns current value of radius,
        otherwise radius is updated as given argument."""
        if not radius_val:
            return self.get_radius()
        elif isinstance(radius_val, (int, float)):
            self.set_radius(radius_val)
            self._diameter = None
            self._area = None

        else:
            raise TypeError('Please provide an integer or  float  for radius of circle')

    def area(self, area_val=None):
        """ if positional argument is not provided it returns current value of area,
        otherwise area of object is updated as given argument."""
        if not area_val:
            return self.get_area()
        elif isinstance(area_val, (int, float)):
            new_radius = sqrt(area_val / pi)
            self.set_radius(new_radius)
            self._diameter = None
            self._area = None
        else:
            raise TypeError('Please provide an integer or float  type for area of circle')

    def diameter(self, diameter_val=None):
        """ if positional argument is not provided it returns current value of diameter,
        otherwise diameter of object is updated as given argument"""
        if not diameter_val:
            return self.get_diameter()
        elif isinstance(diameter_val, (int, float)):
            new_radius = diameter_val / 2
            self.set_radius(new_radius)
            self._area = None
            self._diameter = None
        else:
            raise TypeError('Please provide an integer, float or None type for radius of circle')

    def __str__(self):
        return "Circle({:.2f})".format(self.get_radius())



