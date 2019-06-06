#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """Define inherited list class MyList"""

    def print_sorted(self):
        """prints a list in sorted order"""
        print(sorted(self))
