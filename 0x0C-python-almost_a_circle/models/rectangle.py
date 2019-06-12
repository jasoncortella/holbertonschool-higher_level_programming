#!/usr/bin/python3
"""Define Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Define inherited Base class Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the class.

        Attributes:
        width  (int): Rectangle width
        height (int): Rectangle height
        x      (int): Rectangle corner x coordinate
        y      (int): Rectangle corner y coordinate
        id     (int): Rectangle id

        Raises:
        TypeError if input is not an integer
        ValueError if width or height is under or equals 0
        ValueError if x or y is under 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle."""
        return self.width * self.height

    def display(self):
        """
        Prints rectangle to stdout with the '#' character
        """
        print('\n' * self.y, end='')
        print((' ' * self.x +
              '#' * self.width + '\n') * self.height, end='')

    def __str__(self):
        """Return string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Update Rectangle"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is not None:
                        super().__init__(args[i])
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key is "id":
                    if value is None:
                        super().__init__(args[i])
                    else:
                        self.id = value
                elif key is "width":
                    self.width = value
                elif key is "height":
                    self.height = value
                elif key is "x":
                    self.x = value
                elif key is "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dictionary = {'id': self.id,
                      'width': self.width,
                      'height': self.height,
                      'x': self.x,
                      'y': self.y}
        return dictionary
