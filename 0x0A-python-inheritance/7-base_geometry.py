#!/usr/bin/python3
'''Define a BaseGeometry class'''


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''function that raise an Exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function to validate value
        Args:
            name: name
            value: value of the name
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
