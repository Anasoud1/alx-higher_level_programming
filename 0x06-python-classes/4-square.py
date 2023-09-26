#!/usr/bin/python3
'''Define a class Square'''


class Square:
    '''Define Square'''

    def __init__(self, size=0):
        '''constructor

        Args:
           size (int): new size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Return area of square'''
        return self.__size ** 2
