#!/usr/bin/python3
'''Add all arguments to a Python list and save them to a file.'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if len(sys.argv) == 1:
    li = []
    save_to_json_file(li, "add_item.json")
else:
    s = load_from_json_file("add_item.json")
    s += sys.argv[1:]
    save_to_json_file(s, "add_item.json")
