# 0x06. Python - Classes and Objects
## This directory contains answer files to project 0x06

### 0. My first square
* an empty class Square that defines a square:
* File: 0-square.py

### 1. Square with size
* a class Square that defines a square by: (based on 0-square.py)
* Private instance attribute: size
* Instantiation with size (no type/value verification)
* File: 1-square.py

### 2. Size validation
* a class Square that defines a square by: (based on 1-square.py)
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* File: 2-square.py

### 3. Area of a square
* a class Square that defines a square by: (based on 2-square.py)
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* File: 3-square.py

### 4. Access and update private attribute
* a class Square that defines a square by: (based on 3-square.py)
* Private instance attribute: size:
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* File: 4-square.py

### 5. Printing a square
* a class Square that defines a square by: (based on 4-square.py)
* Private instance attribute: size:
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
* File: 5-square.py

### 6. Coordinates of a square
* a class Square that defines a square by: (based on 5-square.py)
* Private instance attribute: size:
* Private instance attribute: position:
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:

### 7. Singly linked list
* a class Node that defines a node of a singly linked list by:
* Private instance attribute: data:
* Private instance attribute: next_node:
* Instantiation with data and next_node: def __init__(self, data, next_node=None):
* a class SinglyLinkedList that defines a singly linked list:
* File: 100-singly_linked_list.py

### 8. Print Square instance
* a class Square that defines a square by: (based on 6-square.py)
* Private instance attribute: size:
* Private instance attribute: position:
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
* Printing a Square instance should have the same behavior as my_print()
* File: 101-square.py

### 9. Compare 2 squares
* a class Square that defines a square by: (based on 4-square.py)
* Private instance attribute: size:
* Instantiation with size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
* File: 102-square.py

### 10. ByteCode -> Python #5
* File: 103-magic_class.py