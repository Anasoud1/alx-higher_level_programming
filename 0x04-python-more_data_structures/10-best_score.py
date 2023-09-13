#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m = 0
    for value in a_dictionary.values():
        if value > m:
            m = value
    for key, value in a_dictionary.items():
        if value == m:
            return key
