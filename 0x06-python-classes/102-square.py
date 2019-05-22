#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """Initialize the class."""
        self.size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    @property
    def size(self):
        """Gets size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size."""
        if self.__valid_size(value):
            self.__size = value

    def __valid_size(self, size):
        """Checks if a variable is a positive integer."""
        if isinstance(size, int) or isinstance(size, float):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")
        return False

    def __lt__(self, check):
        """Compare 2 sqares area, less than"""
        return (self.area() < check.area())

    def __le__(self, check):
        """Compare 2 sqares area, less than or equal"""
        return (self.area() <= check.area())

    def __eq__(self, check):
        """Compare 2 sqares area, equal"""
        return (self.area() == check.area())

    def __ne__(self, check):
        """Compare 2 sqares area, not equal"""
        return (self.area() != check.area())

    def __gt__(self, check):
        """Compare 2 sqares area, greater than"""
        return (self.area() > check.area())

    def __ge__(self, check):
        """Compare 2 sqares area, greather than or equal"""
        return (self.area() >= check.area())
