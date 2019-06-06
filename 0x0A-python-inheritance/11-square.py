#!/usr/bin/python3
"""Further building of the square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define inhereted BaseGeometry class Rectangle"""
    def __init__(self, size):
        "Initialize"
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the rectangle description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
