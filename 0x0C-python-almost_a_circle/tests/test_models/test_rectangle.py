#!/usr/bin/python3
"""Unittest for base class"""

import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Instantiation(unittest.TestCase):
    """Define unittests for testing instantiation of the Rectangle class"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_rectangle_isinstance(self):
        """Test if rectangle is an instance of base"""
        a = Rectangle(12, 13)
        self.assertIsInstance(a, Base)

    def test_rectangle_no_arg(self):
        """Test creation of rectangle with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        """Test creation of rectangle with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(12)

    def test_rectangle_two_args(self):
        """Test creation of rectangle with two arguments"""
        a = Rectangle(12, 13)
        b = Rectangle(14, 15)
        self.assertEqual(a.id+ 1, b.id)

    def test_rectangle_three_args(self):
        """Test creation of rectangle with three arguments"""
        a = Rectangle(12, 13, 1)
        b = Rectangle(14, 15, 1)
        self.assertEqual(a.id + 1, b.id)

    def test_rectangle_four_args(self):
        """Test creation of rectangle with four arguments"""
        a = Rectangle(12, 13, 1, 2)
        b = Rectangle(14, 15, 1, 3)
        self.assertEqual(a.id + 1, b.id)

    def test_rectangle_five_args(self):
        """Test creation of rectangle with five arguments"""
        a = Rectangle(12, 13, 1, 2, 3)
        self.assertEqual(a.id, 3)

    def test_rectangle_six_plus_args(self):
        """Test creation of rectangle with too many arguments"""
        with self.assertRaises(TypeError):
            Rectangle(12, 13, 1, 2, 3, 4)

    def test_width_private(self):
        """Test if width instance attribute is private"""
        a = Rectangle(12, 13, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__width)

    def test_width_getter(self):
        """Test if width getter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        self.assertEqual(a.width, 12)

    def test_width_setter(self):
        """Test if width setter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        a.width = 69
        self.assertEqual(a.width, 69)

    def test_height_private(self):
        """Test if height instance attribute is private"""
        a = Rectangle(12, 13, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__height)

    def test_height_getter(self):
        """Test if height getter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        self.assertEqual(a.height, 13)

    def test_height_setter(self):
        """Test if height setter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        a.height = 69
        self.assertEqual(a.height, 69)

    def test_x_private(self):
        """Test if x instance attribute is private"""
        a = Rectangle(12, 13, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__x)

    def test_x_getter(self):
        """Test if x getter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        self.assertEqual(a.x, 1)

    def test_x_setter(self):
        """Test if x setter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        a.x = 69
        self.assertEqual(a.x, 69)

    def test_y_private(self):
        """Test if y instance attribute is private"""
        a = Rectangle(12, 13, 1, 2, 3)
        with self.assertRaises(AttributeError):
            print(a.__y)

    def test_y_getter(self):
        """Test if y getter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        self.assertEqual(a.y, 2)

    def test_y_setter(self):
        """Test if y setter works"""
        a = Rectangle(12, 13, 1, 2, 3)
        a.y = 69
        self.assertEqual(a.y, 69)

class TestRectangleAttributes(unittest.TestCase):
    """Define unittests for testing Rectangle class initialization"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_width_neg_int_arg(self):
        """Test Rectangle width attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2, 3, 4)

    def test_height_neg_int_arg(self):
        """Test Rectangle height attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2, 3, 4)

    def test_x_neg_int_arg(self):
        """Test rectangle x attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4)

    def test_y_neg_int_arg(self):
        """Test rectangle y attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_width_zero_arg(self):
        """Test Rectangle width attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3, 4)

    def test_height_zero_arg(self):
        """Test Rectangle height attribute with negative integer argument"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 3, 4)

    def test_width_string_arg(self):
        """Test Rectangle width attribute with string argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2, 3, 4)

    def test_height_string_arg(self):
        """Test Rectangle height attribute with string argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2", 3, 4)

    def test_x_string_arg(self):
        """Test rectangle x attribute with string argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3", 4)

    def test_y_string_arg(self):
        """Test rectangle y attribute with string argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_list_arg(self):
        """Test Rectangle width attribute with list argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 1], 2, 3, 4)

    def test_height_list_arg(self):
        """Test Rectangle height attribute with list argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2, 2], 3, 4)

    def test_x_list_arg(self):
        """Test rectangle x attribute with list argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [3, 3], 4)

    def test_y_list_arg(self):
        """Test rectangle y attribute with list argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [4, 4])

    def test_width_tuple_arg(self):
        """Test Rectangle width attribute with tuple argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 1), 2, 3, 4)

    def test_height_tuple_arg(self):
        """Test Rectangle height attribute with tuple argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (2, 2), 3, 4)

    def test_x_tuple_arg(self):
        """Test rectangle x attribute with tuple argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (3, 3), 4)

    def test_y_tuple_arg(self):
        """Test rectangle y attribute with tuple argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (4, 4))

    def test_width_range_arg(self):
        """Test Rectangle width attribute with range argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(1), 2, 3, 4)

    def test_height_range_arg(self):
        """Test Rectangle height attribute with range argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(2), 3, 4)

    def test_x_range_arg(self):
        """Test rectangle x attribute with range argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(3), 4)

    def test_y_range_arg(self):
        """Test rectangle y attribute with range argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(4))

    def test_width_float_arg(self):
        """Test Rectangle width attribute with float argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.0, 2, 3, 4)

    def test_height_float_arg(self):
        """Test Rectangle height attribute with float argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.0, 3, 4)

    def test_x_float_arg(self):
        """Test rectangle x attribute with float argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 3.0, 4)

    def test_y_float_arg(self):
        """Test rectangle y attribute with range argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.0)

    def test_width_dict_arg(self):
        """Test Rectangle width attribute with dict argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1:1}, 2, 3, 4)

    def test_height_dict_arg(self):
        """Test Rectangle height attribute with dict argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2:2}, 3, 4)

    def test_x_dict_arg(self):
        """Test rectangle x attribute with dict argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {3:3}, 4)

    def test_y_dict_arg(self):
        """Test rectangle y attribute with dict argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {4:4})

    def test_width_bool_arg(self):
        """Test Rectangle width attribute with bool argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2, 3, 4)

    def test_height_bool_arg(self):
        """Test Rectangle height attribute with bool argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True, 3, 4)

    def test_x_bool_arg(self):
        """Test rectangle x attribute with bool argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 4)

    def test_y_bool_arg(self):
        """Test rectangle y attribute with bool argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)

    def test_width_none_arg(self):
        """Test Rectangle width attribute with none argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2, 3, 4)

    def test_height_none_arg(self):
        """Test Rectangle height attribute with none argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None, 3, 4)

    def test_x_none_arg(self):
        """Test rectangle x attribute with none argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 4)

    def test_y_none_arg(self):
        """Test rectangle y attribute with none argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

class TestRectangleArea(unittest.TestCase):
    """Define unittests for testing Rectangle area method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_area(self):
        """Test rectangle area"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, r.area())

    def test_area_args(self):
        """Test rectangle area when args are provided"""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_changed_attributes(self):
        """Test rectangle area when attributes are modified"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        r.height = 7
        self.assertEqual(42, r.area())

class TestRectangleDisplay(unittest.TestCase):
    """Define unittests for testing Rectangle stdout printing"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    @staticmethod
    def captured_output(rectangle):
        output = io.StringIO()
        sys.stdout = output
        rectangle.display()
        sys.stdout = sys.__stdout__
        return output

    def test_regtangle_str_hw(self):
        r = Rectangle(2, 1)
        output = TestRectangleDisplay.captured_output(r)
        verify = "##\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwx(self):
        r = Rectangle(2, 1, 1)
        output = TestRectangleDisplay.captured_output(r)
        verify = " ##\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwxy(self):
        r = Rectangle(2, 1, 1, 1)
        output = TestRectangleDisplay.captured_output(r)
        verify = "\n ##\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwxyi(self):
        r = Rectangle(2, 1, 1, 1, 30)
        output = TestRectangleDisplay.captured_output(r)
        verify = "\n ##\n"
        self.assertEqual(output.getvalue(), verify)


class TestRectangle__str__(unittest.TestCase):
    """Define unittests for testing Rectangle __str__ method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    @staticmethod
    def captured_output(rectangle):
        output = io.StringIO()
        sys.stdout = output
        print(rectangle)
        sys.stdout = sys.__stdout__
        return output

    def test_regtangle_str_hw(self):
        r = Rectangle(4, 6)
        output = TestRectangle__str__.captured_output(r)
        verify = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwx(self):
        r = Rectangle(4, 6, 1)
        output = TestRectangle__str__.captured_output(r)
        verify = "[Rectangle] ({}) 1/0 - 4/6\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwxy(self):
        r = Rectangle(4, 6, 1, 2)
        output = TestRectangle__str__.captured_output(r)
        verify = "[Rectangle] ({}) 1/2 - 4/6\n".format(r.id)
        self.assertEqual(output.getvalue(), verify)

    def test_rectangle_str_hwxyi(self):
        r = Rectangle(4, 6, 1, 2, 30)
        output = TestRectangle__str__.captured_output(r)
        verify = "[Rectangle] (30) 1/2 - 4/6\n"
        self.assertEqual(output.getvalue(), verify)

class TestRectangleUpdate(unittest.TestCase):
    """Define unittests for testing Rectangle args update method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_update_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        verify = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_one_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6)
        verify = "[Rectangle] (6) 3/4 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_two_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7)
        verify = "[Rectangle] (6) 3/4 - 7/2"
        self.assertEqual(str(r), verify)

    def test_update_three_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8)
        verify = "[Rectangle] (6) 3/4 - 7/8"
        self.assertEqual(str(r), verify)

    def test_update_four_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9)
        verify = "[Rectangle] (6) 9/4 - 7/8"
        self.assertEqual(str(r), verify)

    def test_update_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)
        verify = "[Rectangle] (6) 9/10 - 7/8"
        self.assertEqual(str(r), verify)

    def test_update_six_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10, 11)
        verify = "[Rectangle] (6) 9/10 - 7/8"
        self.assertEqual(str(r), verify)

    def test_update_invalid_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "1", 1, 1, 1)

    def test_update_invalid_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "1", 1, 1)

    def test_update_invalid_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "1", 1)

    def test_update_invalid_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "1")

    def test_update_negative_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1, 1, 1, 1)

    def test_update_negative_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1, 1, 1)

    def test_update_negative_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1, 1)

    def test_update_negative_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_zero_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0, 1, 1, 1)

    def test_update_zero_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0, 1, 1)

class TestRectangleUpdateKwargs(unittest.TestCase):
    """Define unittests for testing Rectangle kwargs update method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_update_height_kwarg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(height=99)
        verify = "[Rectangle] (5) 3/4 - 1/99"
        self.assertEqual(str(r), verify)

    def test_update_width_kwarg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(width=99)
        verify = "[Rectangle] (5) 3/4 - 99/2"
        self.assertEqual(str(r), verify)

    def test_update_y_kwarg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(y=99)
        verify = "[Rectangle] (5) 3/99 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_id_kwarg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=99)
        verify = "[Rectangle] (99) 3/4 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_x_kwarg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(x=99)
        verify = "[Rectangle] (5) 99/4 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_two_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=99, x=99)
        verify = "[Rectangle] (99) 99/4 - 1/2"
        self.assertEqual(str(r), verify)

    def test_update_three_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=99, y=99, height=99)
        verify = "[Rectangle] (99) 3/99 - 1/99"
        self.assertEqual(str(r), verify)

    def test_update_four_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=99, x=99, y=99, width=99)
        verify = "[Rectangle] (99) 99/99 - 99/2"
        self.assertEqual(str(r), verify)

    def test_update_five_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=99, x=99, height=99, width=99, y=99)
        verify = "[Rectangle] (99) 99/99 - 99/99"
        self.assertEqual(str(r), verify)


class TestRectangleDict(unittest.TestCase):
    """Define unittests for testing Rectangle dict method"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_dict_no_args(self):
        r = Rectangle(10, 2, 1, 9)
        verify = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), verify)

if __name__ == '__main__':
    unittest.main()
