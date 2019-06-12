#!/usr/bin/python3
"""Unittest for base class"""


import unittest
from models.base import Base


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

if __name__ == '__main__':
    unittest.main()
