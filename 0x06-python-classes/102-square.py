#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """Initialize the class."""
        self.size = size


    def __lt__(self, check):
        return (self.area() < check.area())

    def __le__(self, check):
        return (self.area() <= check.area())

    def __ee__(self, check):
        return (self.area() == check.area())

    def __ne__(self, check):
        return (self.area() != check.area())

    def __gt__(self, check):
        return (self.area() > check.area())

    def __ge__(self, check):
        return (self.area() >= check.area())

    @property
    def size(self):
        """Gets size."""
        return self.__size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

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

    @size.setter
    def size(self, value):
        """Sets size."""
        if self.__valid_size(value):
            self.__size = value
