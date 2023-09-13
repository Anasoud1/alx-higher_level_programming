#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, value in a_dictionary.items():
        new[key] = 2 * value
    return new
