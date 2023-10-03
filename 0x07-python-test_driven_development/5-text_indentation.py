#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    '''function prints a text with 2 new lines after characters: ., ? and :
    Args: 
        text: text to print
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == ' ' and text[i + 1] == ' ': 
                while text[i] == ' ':
                    i += 1
        if text[i] in ['.', '?', ':']:
            print("{}\n".format(text[i]))
            i += 1
            while text[i] == ' ':
               i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1
