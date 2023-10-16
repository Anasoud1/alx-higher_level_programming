#!/usr/bin/python3
'''Define a class Base'''
import json


class Base:
    '''class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor
        Args:
            id: new id
        '''
        if (id is None):
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
