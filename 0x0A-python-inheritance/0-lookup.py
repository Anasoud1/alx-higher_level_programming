#!/usr/bin/python3
'''Define a method lookup'''


def lookup(obj):
    '''Function that returns the list of available attributes and methods
    of an object
    Args:
        obj: object'''

    return dir(obj)
