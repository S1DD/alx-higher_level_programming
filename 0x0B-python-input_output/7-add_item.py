#!/usr/bin/python3

import sys
"""Adds all arguments to a Python list, ans then save them to a file"""
if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file.py').load_from_json_file

    try:
        items = load_from_json("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(item, "add_item.json")
