#!/usr/bin/python3
'''Define a class Base'''


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
