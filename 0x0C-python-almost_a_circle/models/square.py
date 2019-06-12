#!/usr/bin/python3
"""Define Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define inherited Rectangle class Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the class.

        Attributes:
        size  (int): Rectangle height and width
        x     (int): Rectangle corner x coordinate
        y     (int): Rectangle corner y coordinate
        id    (int): Rectangle id

        Raises:
        TypeError if input is not an integer
        ValueError if width or height is under or equals 0
        ValueError if x or y is under 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets width."""
        self.width = value
        self.height = value

    def area(self):
        """Returns area of the rectangle."""
        return self.width ** 2

    def display(self):
        """
        Prints square to stdout with the '#' character
        """
        print('\n' * self.y, end='')
        print((' ' * self.x +
              '#' * self.width + '\n') * self.height, end='')

    def __str__(self):
        """Return string representation of rectangle"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Update square"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key is "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key is "size":
                    self.width = value
                elif key is "x":
                    self.x = value
                elif key is "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dictionary2 = {'id': self.id,
                       'size': self.width,
                       'x': self.x,
                       'y': self.y}
        return dictionary2
