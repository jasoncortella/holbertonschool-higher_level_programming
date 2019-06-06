#!/usr/bin/python3

class MyInt(int):
    """Define inhereted int class MyInt"""
    def __eq__(self, value):
        return self.real != value
    def __ne__(self, value):
        return self.real == value
