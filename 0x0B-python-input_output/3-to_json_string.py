#!/usr/bin/python3
'''Define to_json_string function'''
import json


def to_json_string(my_obj):
    '''Returns the JSON representation of an object
    Args:
        my_obj: object to JSON
    '''
    return json.dumps(my_obj)
