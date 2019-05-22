#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class."""
        self.size = size
        self.position = position

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
        if isinstance(size, int):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        return False

    @property
    def position(self):
        """Gets position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position."""
        if self.__valid_position(value):
            self.__position = value

    def __valid_position(self, position):
        """Checks if a variable is a tuple of 2 positive integers."""
        if isinstance(position, tuple):
            if len(position) == 2:
                if isinstance(position[0], int):
                    if isinstance(position[1], int):
                        if position[0] >= 0 <= position[1]:
                            return True
        raise TypeError("position must be a tuple of 2 positive integers")
        return False

    def my_print(self):
        """Prints the square, accounting for size and position"""
        if self.__size == 0:
            print()
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """The square in string format"""
        if self.size == 0:
            return ""
        string1 = '\n' * self.__position[1]
        string2 = ' ' * self.__position[0] + '#' * self.__size + '\n'
        string = string1 + string2 * self.__size
        return string[:-1]
