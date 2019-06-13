#!/usr/bin/python3
"""Unittest for base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Instantiation(unittest.TestCase):
    """Define unittests for testing instantiation of the Base class"""

    def setUp(self):
        """Reset nb_instances to 0"""
        Base.test_reset()

    def test_id_no_arg_first(self):
        """Test base id when no argument given, first time through"""
        a = Base()
        self.assertEqual(a.id, 1)

    def test_id_no_arg_continue(self):
        """Test base id when no argument given"""
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id + 2, c.id)

    def test_id_int_arg(self):
        """Test base id, with integer argument"""
        a = Base(12)
        self.assertEqual(a.id, 12)

    def test_id__nb_instances_continuation(self):
        """Test base id, with bool argument"""
        a = Base()
        b = Base(12)
        c = Base()
        self.assertEqual(a.id + 1, c.id)

    def test_id_same_arg(self):
        """Test base id, with integer argument, with overlap"""
        a = Base(12)
        b = Base(12)
        self.assertEqual(a.id, b.id)

    def test_id_string_arg(self):
        """Test base id, with string argument"""
        a = Base('12')
        self.assertEqual(a.id, '12')

    def test_id_list_arg(self):
        """Test base id, with list argument"""
        a = Base([12, 13])
        self.assertEqual(a.id, [12, 13])

    def test_id_tuple_arg(self):
        """Test base id, with tuple argument"""
        a = Base((12, 13))
        self.assertEqual(a.id, (12, 13))

    def test_id_range_arg(self):
        """Test base id, with range argument"""
        a = Base(range(3))
        self.assertEqual(a.id, range(0, 3))

    def test_id_float_arg(self):
        """Test base id, with float argument"""
        a = Base(12.0)
        self.assertEqual(a.id, 12.0)

    def test_id_dict_arg(self):
        """Test base id, with dict argument"""
        a = Base({12:13})
        self.assertEqual(a.id, {12:13})

    def test_id_bool_arg(self):
        """Test base id, with bool argument"""
        a = Base(True)
        self.assertEqual(a.id, True)

    def test_id_none_arg(self):
        """Test base id, with 'None' argument"""
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id + 1, b.id)

    def test_id_public(self):
        """Test if id instance is public"""
        a = Base(12)
        a.id = 13
        self.assertEqual(a.id, 13)

    def test_nb_instances_private(self):
        """Test if nb_instances attribute is private"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_invalid_arg_count(self):
        """Test if arg count is greater than 1"""
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBaseToJSON(unittest.TestCase):
    """Define unittests for testing to_json_string method of the Base class"""

    def test_to_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 1)

    def test_to_json_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_type_rectangle(self):
        r = Rectangle(10, 700, 2, 8)
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_one_dict_rectangle(self):
        r = Rectangle(10, 700, 2, 8)
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(len(json_dictionary), 55)

    def test_to_json_two_dicts_rectangle(self):
        r1 = Rectangle(10, 700, 2, 8)
        r2 = Rectangle(10, 700, 2, 8)
        json_dictionary = Base.to_json_string([r1.to_dictionary(),
                                               r2.to_dictionary()])
        self.assertEqual(len(json_dictionary), 112)

    def test_to_json_three_dicts_rectangle(self):
        r1 = Rectangle(10, 700, 2, 8)
        r2 = Rectangle(10, 700, 2, 8)
        r3 = Rectangle(10, 7, 2, 8)
        json_dictionary = Base.to_json_string([r1.to_dictionary(),
                                               r2.to_dictionary(),
                                               r3.to_dictionary()])
        self.assertEqual(len(json_dictionary), 163)

    def test_to_json_type_Square(self):
        r = Square(10, 2, 8)
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_one_dict_Square(self):
        r = Square(10, 2, 8)
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(len(json_dictionary), 39)

    def test_to_json_two_dicts_Square(self):
        r1 = Square(10, 2, 8)
        r2 = Square(10, 2, 8)
        json_dictionary = Base.to_json_string([r1.to_dictionary(),
                                               r2.to_dictionary()])
        self.assertEqual(len(json_dictionary), 79)

    def test_to_json_three_dicts_Square(self):
        r1 = Square(10, 2, 8)
        r2 = Square(10, 2, 8)
        r3 = Square(10, 2, 8)
        json_dictionary = Base.to_json_string([r1.to_dictionary(),
                                               r2.to_dictionary(),
                                               r3.to_dictionary()])
        self.assertEqual(len(json_dictionary), 117)

class TestBaseToJSONtoFile(unittest.TestCase):
    """Define unittests for testing save_to_file method of the Base class"""

    @classmethod
    def setUp(self):
        """Delete created files and reset nb counter"""
        Base.test_reset()
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass
        try:
            os.remove("Base.json")
        except:
            pass


    def test_to_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 1)

    def test_file_json_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_file_json_Empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_file_json_one_dict_rectangle(self):
        r = Rectangle(10, 700, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 55)

    def test_file_json_one_dict_Square(self):
        r = Square(10, 2, 8)
        Square.save_to_file([r])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 39)

    def test_file_json_two_dict_rectangle(self):
        r1 = Rectangle(10, 700, 2, 8)
        r2 = Rectangle(10, 700, 2, 8)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 110)

    def test_file_json_two_dict_Square(self):
        r1 = Square(10, 2, 8)
        r2 = Square(10, 2, 8)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 78)

    def test_file_json_one_dict_Square_overwrite(self):
        r = Square(10, 2, 8)
        Square.save_to_file([r])
        Square.save_to_file([r])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 39)


class TestBaseJSONstringToDictionary(unittest.TestCase):
    """Define unittests for testing from_json_string method of the Base class"""

    def test_from_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_two_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 1)

    def test_from_json_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_Empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_rectangle(self):
        json_str = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        json_list = Rectangle.to_json_string(json_str)
        json_str_2 = Rectangle.from_json_string(json_list)
        self.assertEqual(json_str, json_str_2)

    def test_from_json_square(self):
        json_str = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        json_list = Square.to_json_string(json_str)
        json_str_2 = Square.from_json_string(json_list)
        self.assertEqual(json_str, json_str_2)

    def test_from_json_two_rectangle(self):
        json_str = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                    {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        json_list = Rectangle.to_json_string(json_str)
        json_str_2 = Rectangle.from_json_string(json_list)
        self.assertEqual(json_str, json_str_2)

    def test_from_json_two_square(self):
        json_str = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                    {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        json_list = Square.to_json_string(json_str)
        json_str_2 = Square.from_json_string(json_list)
        self.assertEqual(json_str, json_str_2)

if __name__ == '__main__':
    unittest.main()
