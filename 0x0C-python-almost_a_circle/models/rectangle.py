#!/usr/bin/python3
'''Define a class Rectangle'''
from models.base import Base
import json


class Rectangle(Base):
    '''class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor
        Args:
            width: new width
            height: new height
            x: new x
            y: new y
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area value of the Rectangle'''
        return self.width * self.height

    def display(self):
        '''print in stdout the Rectangle instance'''
        for i in range(self.y):
            print()
        for h in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        '''return representation of the class'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args:
            i = 0
            for arg in args:
                i += 1
            if i >= 1:
                setattr(self, "id", args[0])
            if i >= 2:
                setattr(self, "width", args[1])
            if i >= 3:
                setattr(self, "height", args[2])
            if i >= 4:
                setattr(self, "x", args[3])
            if i >= 5:
                setattr(self, "y", args[4])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
