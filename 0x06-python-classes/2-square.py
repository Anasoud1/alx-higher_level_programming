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
