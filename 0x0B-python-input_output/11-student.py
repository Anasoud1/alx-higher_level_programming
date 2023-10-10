#!/usr/bin/python3
'''Define a class Student'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''Constuctor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return a dictionary representation of a Student'''
        dic = self.__dict__
        if attrs is None:
            return dic
        new = {}
        for key, value in dic.items():
            if key in attrs:
                new[key] = value
        return new

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            if key == self.first_name:
                self.fist_name = value
            elif key == self.last_name:
                self.last_name = value
            elif key == self.age:
                self.age = value
