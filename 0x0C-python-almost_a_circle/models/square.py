#!/usr/bin/python3
'''Define a class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor
        Args:
            size: new size
            x: new x
            y: new y
            id: new id
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        '''return representation of the class'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        '''assigns attributes'''
    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args:
            i = 0
            for arg in args:
                i += 1
            if i >= 1:
                setattr(self, "id", args[0])
            if i >= 2:
                setattr(self, "size", args[1])
            if i >= 3:
                setattr(self, "x", args[2])
            if i >= 4:
                setattr(self, "y", args[3])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}
