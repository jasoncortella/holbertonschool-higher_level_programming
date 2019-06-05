# 0x0A. Python - Inheritance
## This directory contans answer files to Holberton School Python project 0x0A

### 0. Lookup
* a function that returns the list of available attributes and methods of an object:
* Prototype: def lookup(obj):
* File: 0-lookup.py

### 1. My list
* a class MyList that inherits from list:
* def print_sorted(self):
* File: 1-my_list.py, tests/1-my_list.txt

### 2. Exact same object
* a function that returns True if the object is exactly an instance of the specified class ; otherwise False
* Prototype: def is_same_class(obj, a_class):
* File: 2-is_same_class.py

### 3. Same class or inherit from
* a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
* Prototype: def is_kind_of_class(obj, a_class):
* File: 3-is_kind_of_class.py

### 4. Only sub class of
* a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
* Prototype: def inherits_from(obj, a_class):
* File: 4-inherits_from.py

### 5. Geometry module
* an empty class BaseGeometry.
* File: 5-base_geometry.py

### 6. Improve Geometry
* a class BaseGeometry (based on 5-base_geometry.py).
* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* File: 6-base_geometry.py

### 7. Integer validator
* a class BaseGeometry (based on 6-base_geometry.py).
* Public instance method: def integer_validator(self, name, value): that validates value:
* File: 7-base_geometry.py, tests/7-base_geometry.txt

### 8. Rectangle
* a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
* File: 8-rectangle.py

### 9. Full rectangle
* a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
* File: 9-rectangle.py

### 10. Square #1
* a class Square that inherits from Rectangle (9-rectangle.py):
* File: 10-square.py

### 11. Square #2
* a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
* File: 11-square.py

### 12. My integer
* a class MyInt that inherits from int:
* MyInt is a rebel. MyInt has == and != operators inverted
* File: 100-my_int.py

### 13. Can I?
* a function that adds a new attribute to an object if it’s possible:
* Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
* Does not use try/catch
* File: 101-add_attribute.py