#!/usr/bin/python3
'''Define a load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”
    Args:
        filename: file name
    '''
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
