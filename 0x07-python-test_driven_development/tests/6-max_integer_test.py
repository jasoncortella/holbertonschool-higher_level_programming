#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_ordered_negative_list(self):
        """Test an ordered list of negative integers."""
        negative_ordered = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative_ordered), -1)

    def test_unordered_negative_list(self):
        """Test an unordered list of negative integers."""
        negative_unordered = [-1, -3, -4, -2]
        self.assertEqual(max_integer(negative_unordered), -1)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_single_element_list(self):
        """Test a list with one element."""
        single_element_list = [12]
        self.assertEqual(max_integer(single_element_list), 12)

    def test_float_list(self):
        """Test a list with floats."""
        float_list = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(max_integer(float_list), 4.0)

    def test_floats_and_ints(self):
        """Test a list with floats and ints."""
        float_and_int_list = [1.0, 2, 3.0, 4]
        self.assertEqual(max_integer(float_and_int_list), 4)

    def test_string_list(self):
        """Test a list of strings."""
        string_list = ['a', 'b', 'c', 'd']
        self.assertEqual(max_integer(string_list), 'd')

    def test_string(self):
        """Test a single string."""
        string = ['Hello']
        self.assertEqual(max_integer(string), 'Hello')

if __name__ == '__main__':
    unittest.main()
