#!/usr/bin/python3
"""Defines a class - Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize

        Args:
        first_name (str): Student's first name
        last_name  (str): Student's last name
        age        (int): Student's age

        Returns:
        Nothing.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dict representation of Student instance

        Args:
        None.

        Returns:
        Dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in attrs:
            try:
                new_dict[key] = self.__dict__[key]
            except:
                pass
        return new_dict
