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
