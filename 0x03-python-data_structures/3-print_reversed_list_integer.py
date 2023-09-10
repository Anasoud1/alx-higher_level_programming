#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if not my_list:
        return None
    for i in my_list:
        print("{:d}".format(i))
