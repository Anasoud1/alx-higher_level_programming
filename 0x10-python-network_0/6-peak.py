#!/usr/bin/python3
"""function find_peak """


def find_peak(list_of_integers):
    """function that find a peak in a list"""
    if not list_of_integers:
        return None
    return max(list_of_integers)
