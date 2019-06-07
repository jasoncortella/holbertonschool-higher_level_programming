#!/usr/bin/python3
"""Function generate a list representing Pascal's Triangle"""


def pascal_triangle(n):
    """Generates a pascal's triangle list

    Args:
    n (int): Size of the triangle to generate

    Returns:
    Generated list
    """
    lastrow = []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i // 2 + 1):
            row[j] = lastrow[j - 1] + lastrow[j]
            row[i - j] = lastrow[j - 1] + lastrow[j]
        triangle.append(row)
        lastrow = row
    return triangle
