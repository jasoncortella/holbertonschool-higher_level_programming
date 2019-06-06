#!/usr/bin/python3
"""Define class MyInt based on int. Reverse == and != functions"""


class MyInt(int):
    """Define inhereted int class MyInt"""

    def __eq__(self, value):
        """Swap == for !="""
        return self.real != value

    def __ne__(self, value):
        """Swap != for =="""
        return self.real == value
