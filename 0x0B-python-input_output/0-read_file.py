#!/usr/bin/python3
'''Define read_file function'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file name
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
