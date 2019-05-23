#!/usr/bin/python3


def matrix_mul(m_a, m_b):

    """
    matrix_mul - multiplies two matrices.

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        A new matrix

    Raises:
        - TypeError if either arg is not a list
        - TypeError if either list contains non list elements
        - ValueError if either list is empty
        - TypeError if any list - list element is not an int or float
        - TypeError if m_a or m_b has non uniform row size
        - ValueError if m_a and m_b cannot be multiplied
    """
