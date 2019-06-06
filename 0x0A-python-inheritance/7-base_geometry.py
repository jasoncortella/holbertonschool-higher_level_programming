#!/usr/bin/python3
"""Further building upon the class"""


class BaseGeometry:
    """Define BaseGeometry class"""
    def area(self):
        """Return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer to be greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
