#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """Initialize the class."""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)
