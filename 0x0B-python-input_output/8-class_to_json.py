#!/usr/bin/python3
'''Define class_to_json function'''


def class_to_json(obj):
    '''returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
    obj: instance of a Class
    '''
    return obj.__dict__
