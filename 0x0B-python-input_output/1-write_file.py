#!/usr/bin/python3
'''Define write_file function'''


def write_file(filename="", text=""):
    '''writes a string to a text file
    Args:
        filename: file name
        text: string to write
    Return: number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return num
