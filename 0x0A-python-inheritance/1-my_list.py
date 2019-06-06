#!/usr/bin/python3
"""A module"""

class MyList(list):
    """Define inherited list class MyList"""

    def print_sorted(self):
        """prints a list in sorted order"""
        print(sorted(self))
