#!/usr/bin/python3
'''Define a class MyList'''


class MyList(list):
    '''prints the list sorted'''
    def print_sorted(self):
        '''Print a list in sorted ascending order'''
        print(sorted(self))
