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

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if any(not isinstance(elm, (int, float))
           for elm in [x for row in m_a for x in row]):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(elm, (int, float))
           for elm in [x for row in m_b for x in row]):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_b_invert = []
    for i in range(len(m_b[0])):
        inverted_row = []
        for j in range(len(m_b)):
            inverted_row.append(m_b[j][i])
        m_b_invert.append(inverted_row)

    ret_matrix = []
    for row_a in m_a:
        new_row = []
        for row_b in m_b_invert:
            result = 0
            for i in range(len(m_b_invert[0])):
                result += row_a[i] * row_b[i]
            new_row.append(result)
        ret_matrix.append(new_row)

    return ret_matrix
