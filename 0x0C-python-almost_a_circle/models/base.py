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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        new = []
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is not None:
                for obj in list_objs:
                    new.append(obj.to_dictionary())
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string'''
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if dictionary:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        try:
            with open("{}.json".format(cls.__name__), encoding="utf-8") as f:
                list_dict = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        new = []
        for dic in list_dict:
            obj = cls.create(**dic)
            new.append(obj)
        return new
