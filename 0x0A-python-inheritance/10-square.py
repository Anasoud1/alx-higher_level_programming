#!/usr/bin/python3
'''Defines a class square that inherits from Rectangle.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''return area of a square'''
        return self.__size * self.__size

    def __str__(self):
        '''return area description'''
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
