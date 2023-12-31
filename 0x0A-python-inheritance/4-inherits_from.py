#!/usr/bin/python3
'''Define a inherits_from methid'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.'''

    return not type(obj) == a_class and isinstance(obj, a_class)
