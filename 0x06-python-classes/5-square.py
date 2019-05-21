#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """Initialize the class."""
        self.__size = size

    @property
    def size(self):
        """Gets size."""
        return self.__size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square, accounting for size"""
        if self.__size == 0:
            print()
        print(('#' * self.__size + '\n') * self.__size, end='')

    def __valid_size(self, size):
        """Checks if a variable is a positive integer."""
        if isinstance(size, int):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        return False

    @size.setter
    def size(self, value):
        """Sets size."""
        if self.__valid_size(value):
            self.__size = value
