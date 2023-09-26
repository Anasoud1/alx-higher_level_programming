#!/usr/bin/python3
'''Define a class Square'''


class Square:
    '''Define Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''constructor

        Args:
           size (int): new size
           position : tuple with 2 integer
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def postion(self):
        return self.__position
    
    @postion.setter
    def postion(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return area of square'''
        return self.__size ** 2

    def my_print(self):
        '''print square with # charactere'''
        space = ""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[0]):
                space += " "
            for i in range(self.size):
                print("{}".format(space), end="")
                for j in range(self.size):
                    print("#", end="")
                print()
