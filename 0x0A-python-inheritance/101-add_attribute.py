#!/usr/bin/python3
'''define add_attribute method'''


def add_attribute(ob, attr, value):
    '''adds a new attribute to an object if it’s possible
    Args:
        ob: object to add
        attr1 : attribute
        value: value of the attribute
    '''
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, attr, value)
