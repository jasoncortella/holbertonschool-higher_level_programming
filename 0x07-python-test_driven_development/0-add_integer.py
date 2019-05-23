#!/usr/bin/python3


def add_integer(a, b=98):

    """
    add_integer - Adds and returns two integers

    *** Floats are cast to ints before addition ***

    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        The sum of a and b

    Raises:
        - TypeError if a or b are not and int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
