#!/usr/bin/python3
'''define a class MyInt'''


class MyInt(int):
    '''invert == and != in MyInt'''
    def __eq__(self, value):
        '''change == operator to !='''
        return self.real != value

    def __ne__(self, value):
        '''change != operator to =='''
        return self.real == value
