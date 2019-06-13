#!/usr/bin/python3
"""Unittest for base class"""

import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare_Instantiation(unittest.TestCase):
    """Define unittests for testing instantiation of the Rectangle class"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_square_isinstance(self):
        """Test if squre is an instance of rectangle"""
        a = Square(12, 13)
        self.assertIsInstance(a, Rectangle)

    def test_square_no_arg(self):
        """Test creation of square with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_square_one_arg(self):
        """Test creation of square with one argument"""
        a = Square(12)
        b = Square(13)
        self.assertEqual(a.id+ 1, b.id)

    def test_square_two_args(self):
        """Test creation of square with two arguments"""
        a = Square(12, 1)
        b = Square(13, 1)
        self.assertEqual(a.id + 1, b.id)

    def test_square_three_args(self):
        """Test creation of square with three arguments"""
        a = Square(12, 1, 2)
        b = Square(13, 1, 2)
        self.assertEqual(a.id + 1, b.id)

    def test_square_four_args(self):
        """Test creation of square with four arguments"""
        a = Square(12, 1, 2, 3)
        self.assertEqual(a.id, 3)

    def test_square_five_plus_args(self):
        """Test creation of square with too many arguments"""
        with self.assertRaises(TypeError):
            Square(12, 13, 1, 2, 3, 4)

    def test_square_width_private(self):
        """Test if square width instance attribute is private"""
        a = Square(12, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__width)

    def test_square_width_getter(self):
        """Test if square width getter works"""
        a = Square(12, 1, 2, 3)
        self.assertEqual(a.width, 12)

    def test_square_width_setter(self):
        """Test if square width setter works"""
        a = Square(12, 1, 2, 3)
        a.width = 69
        self.assertEqual(a.width, 69)

    def test_square_size_getter(self):
        """Test if square size getter works"""
        a = Square(12, 1, 2, 3)
        self.assertEqual(a.size, 12)

    def test_square_x_private(self):
        """Test if square x instance attribute is private"""
        a = Square(12, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__x)

    def test_square_x_getter(self):
        """Test if square x getter works"""
        a = Square(12, 1, 2, 3)
        self.assertEqual(a.x, 1)

    def test_square_x_setter(self):
        """Test if x setter works"""
        a = Square(12, 1, 2, 3)
        a.x = 69
        self.assertEqual(a.x, 69)

    def test_y_private(self):
        """Test if y instance attribute is private"""
        a = Square(12, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__y)

    def test_y_getter(self):
        """Test if square y getter works"""
        a = Square(12, 1, 2, 3)
        self.assertEqual(a.y, 2)

    def test_y_setter(self):
        """Test if square y setter works"""
        a = Square(12, 1, 2, 3)
        a.y = 69
        self.assertEqual(a.y, 69)

class TestSquareUpdate(unittest.TestCase):
    """Define unittests for testing Rectangle args update method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_square_update_no_args(self):
        r = Square(5)
        r.update()
        verify = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(r), verify)

    def test_square_update_one_args(self):
        r = Square(5)
        r.update(10)
        verify = "[Square] (10) 0/0 - 5"
        self.assertEqual(str(r), verify)

    def test_square_update_two_args(self):
        r = Square(5)
        r.update(1, 2)
        verify = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(r), verify)

    def test_square_update_three_args(self):
        r = Square(5)
        r.update(1, 2, 3)
        verify = "[Square] (1) 3/0 - 2"
        self.assertEqual(str(r), verify)

    def test_square_update_four_args(self):
        r = Square(5)
        r.update(1, 2, 3, 4)
        verify = "[Square] (1) 3/4 - 2"
        self.assertEqual(str(r), verify)

    def test_square_update_invalid_size(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "1", 1, 1, 1)

    def test_square_update_invalid_x(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, "1", 1)

    def test_square_update_invalid_y(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, "1")

    def test_square_update_negative_size(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1, 1, 1)

    def test_square_update_negative_x(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, -1, 1)

    def test_square_update_negative_y(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, -1)

    def test_square_update_zero_size(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0, 1, 1)

class TestSquareDict(unittest.TestCase):
    """Define unittests for testing Rectangle dict method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_square_dict_no_args(self):
        r = Square(10, 1, 9)
        verify = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(r.to_dictionary(), verify)

if __name__ == '__main__':
    unittest.main()
