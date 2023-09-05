#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ""
    while i < len(str):
        if i != n:
            new_str = new_str + str[i]
        i += 1
    return new_str
