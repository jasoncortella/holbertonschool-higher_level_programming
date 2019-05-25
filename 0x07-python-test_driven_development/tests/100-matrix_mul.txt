>>> matrix_mul = __import__('100-matrix_mul').matrix_mul

>>> m_a = [
... [1, 2],
...     [3, 4],
...     ]
>>> m_b = m_a
>>> matrix_mul(m_a, m_b)
[[7, 10], [15, 22]]

>>> m_a = [
... [1, 2]
...     ]
>>> m_b = [
... [3, 4],
...     [5, 6],
...     ]
>>> matrix_mul(m_a, m_b)
[[13, 16]]

>>> m_a = [
... [1.1, 2.2]
...     ]
>>> m_b = [
... [3.3, 4.4],
...     [5.5, 6.6],
...     ]
>>> matrix_mul(m_a, m_b)
[[15.73, 19.36]]

>>> m_a = [
... [1, 2.2]
...     ]
>>> m_b = [
... [3, 4.4],
...     [5.5, 6],
...     ]
>>> matrix_mul(m_a, m_b)
[[15.100000000000001, 17.6]]

>>> m_a = [
... ["1", 2.2]
...     ]
>>> m_b = [
... [3, 4.4],
...     [5.5, "6"],
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_a should contain only integers or floats

>>> m_a = []
>>> m_b = [
... [3, 4.4],
...     [5.5, "6"],
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: m_a can't be empty

>>> m_a = [
... ["1", 2.2]
...     ]
>>> m_b = []
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: m_b can't be empty

>>> m_a = 3
>>> m_b = [1, 2]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_a must be a list

>>> m_a = [1, 2]
>>> m_b = 3
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_b must be a list

>>> m_a = [1, 2]
>>> m_b = [
... [3, 4],
...     [5, 6]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_a must be a list of lists

>>> m_b = [1, 2]
>>> m_a = [
... [3, 4],
...     [5, 6]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_b must be a list of lists

>>> m_a = [
... [3, 4],
...     [5, 6]
...     ]
>>> m_b = [
... ["3", 4],
...     [5, 6]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: m_b should contain only integers or floats

>>> m_a = [
... [3, 4, 5],
...     [5, 6]
...     ]
>>> m_b = [
... [3, 4],
...     [5, 6]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: each row of m_a must should be of the same size

>>> m_a = [
... [3, 4],
...     [5, 6]
...     ]
>>> m_b = [
... [3, 4, 5],
...     [5, 6]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: each row of m_b must should be of the same size

>>> m_a = [
... [3, 4, 5, 6, 7, 8],
...     [5, 6, 7, 8, 9, 10]
...     ]
>>> m_b = [
... [3, 4, 5, 6],
...     [5, 6, 7, 8]
...     ]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: m_a and m_b can't be multiplied

>>> matrix_mul(m_a)
Traceback (most recent call last):
TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

>>> matrix_mul()
Traceback (most recent call last):
TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
