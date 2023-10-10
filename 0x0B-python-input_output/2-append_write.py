#!/usr/bin/python3
'''Define a append_write function'''


def append_write(filename="", text=""):
    ''' appends a string at the end of a text file
    Args:
        filename: file name
        text: string to write
    Return: number of characters added
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
