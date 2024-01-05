#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    '''function that prints a square with the character #
    Args:
        size: size of square
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format('#' * size))
