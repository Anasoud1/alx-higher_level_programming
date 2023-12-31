#!/usr/bin/python3
'''Define a append_after function'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file, after each line containing
    a specific string'''
    text = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
