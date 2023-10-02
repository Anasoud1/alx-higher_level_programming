#!/usr/bin/python3
'''Define class Rectangle'''


class Rectangle:
    '''Define class Rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Constructor
        Args:
            self.width = new width
            self.height = new height
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''getter for the private instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for the private instance attribute width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for the private instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for the private instance attribute height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return area of rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Return perimeter of rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''function print rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        sym = str(self.print_symbol) * self.width
        return "\n".join(sym for h in range(self.height))

    def __repr__(self):
        '''function represente rectangle'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''function that print msg after deleting an instance of Rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

