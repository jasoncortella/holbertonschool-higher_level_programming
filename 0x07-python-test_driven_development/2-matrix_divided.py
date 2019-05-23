#!/usr/bin/python3


def matrix_divided(matrix, div):

    """
    matrix_divided - divides all elements of a matrix.

    *** All division results rounded to 2 decimal places  ***

    Args:
        matrix: The matrix to perform upon
        div: The value to divide the matrix elements by

    Returns:
        A new matrix

    Raises:
        - TypeError if any element of the matrix is not an int or float
        - TypeError of the matrix rows are not of uniform size
        - TypeError if div is not a number
        - ZeroDivisionError if div == 0
    """
