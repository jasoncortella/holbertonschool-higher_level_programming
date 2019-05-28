# 0x08. Python - More Classes and Objects

### 0. Simple rectangle
* File: 0-rectangle.py
* an empty class Rectangle that defines a rectangle:

### 1. Real definition of a rectangle
* File: 1-rectangle.py
* Private instance attribute: width:
* property def width(self): to retrieve it
* property setter def width(self, value): to set it:
* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
* property def height(self): to retrieve it
* property setter def height(self, value): to set it:
* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):

### 2. Area and Perimeter
* File: 2-rectangle.py
* Above, plus...
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
* if width or height is equal to 0, perimeter is equal to 0

### 3. String representation
* File: 3-rectangle.py
* Above, plus...
* print() and str() should print the rectangle with the character #
* if width or height is equal to 0, return an empty string

### 4. Eval is magic
* File: 4-rectangle.py
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()

### 5. Detect instance deletion
* File: 5-rectangle.py
* Above, plus...
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

### 6. How many instances
* File: 6-rectangle.py
* Above, plus...
* Public class attribute number_of_instances:
* Initialized to 0
* Incremented during each new instance instantiation
* Decremented during each instance deletion

### 7. Change representation
* File: 7-rectangle.py
* Above, plus...
* Public class attribute print_symbol:
* Initialized to #
* Used as symbol for string representation
* Can be any type

### 8. Compare rectangles
* File: 8-rectangle.py
* Above, plus...
* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
* rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
* rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
* Returns rect_1 if both have the same area value

### 9. A square is a rectangle
* File: 9-rectangle.py
* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
