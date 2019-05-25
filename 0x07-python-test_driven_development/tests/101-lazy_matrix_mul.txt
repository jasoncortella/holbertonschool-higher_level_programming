>>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
>>> m_a = [
... [1, 2],
...    [3, 4]
...     ]
>>> m_b = m_a
>>> lazy_matrix_mul(m_a, m_b)
array([[ 7, 10],
       [15, 22]])

>>> m_a = [
...  [1, 2]
...     ]
>>> m_b = [
... [3, 4],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
array([[13, 16]])

>>> m_a = [
... [1.1, 2.2]
... ]
>>> m_b = [
... [3.3, 4.4],
... [5.5, 6.6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
array([[15.73, 19.36]])

>>> m_a = [
... [1, 2.2]
... ]
>>> m_b = [
... [3, 4.4],
... [5.5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
array([[15.1, 17.6]])

>>> m_a = [
... ["1", 2.2]
... ]
>>> m_b = [
... [3, 4.4],
... [5.5, "6"]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: ufunc 'matmul' did not contain a loop with signature matching types dtype('<U32') dtype('<U32') dtype('<U32')

>>> m_a = []
>>> m_b = [
... [3, 4.4],
... [5.5, "6"]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 0)

>>> m_a = [
... ["1", 2.2]
... ]
>>> m_b = []
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 0 is different from 2)

>>> m_a = 3
>>> m_b = [1, 2]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: matmul: Input operand 0 does not have enough dimensions (has 0, gufunc core with signature (n?,k),(k,m?)->(n?,m?) requires 1)

>>> m_a = [1, 2]
>>> m_b = 3
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: matmul: Input operand 1 does not have enough dimensions (has 0, gufunc core with signature (n?,k),(k,m?)->(n?,m?) requires 1)

>>> m_a = [1, 2]
>>> m_b = [
... [3, 4],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
array([13, 16])

>>> m_b = [1, 2]
>>> m_a = [
... [3, 4],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
array([11, 17])

>>> m_a = [
... [3, 4],
... [5, 6]
... ]
>>> m_b = [
... ["3", 4],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: ufunc 'matmul' did not contain a loop with signature matching types dtype('<U21') dtype('<U21') dtype('<U21')

>>> m_a = [
... [3, 4, 5],
... [5, 6]
... ]
>>> m_b = [
... [3, 4],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: ufunc 'matmul' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

>>> m_a = [
... [3, 4],
... [5, 6]
... ]
>>> m_b = [
... [3, 4, 5],
... [5, 6]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
TypeError: ufunc 'matmul' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

>>> m_a = [
... [3, 4, 5, 6, 7, 8],
... [5, 6, 7, 8, 9, 10]
... ]
>>> m_b = [
... [3, 4, 5, 6],
... [5, 6, 7, 8]
... ]
>>> lazy_matrix_mul(m_a, m_b)
Traceback (most recent call last):
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 6)

>>> lazy_matrix_mul(m_a)
Traceback (most recent call last):
TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'

>>> lazy_matrix_mul()
Traceback (most recent call last):
TypeError: lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
