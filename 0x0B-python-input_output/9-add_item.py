#!/usr/bin/python3
""" LoadAddSave Module
script that adds all arguments
to a Python list, and then save
them to a file
"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    l = load_from_json_file('add_item.json')
except:
    l = []

if len(sys.argv) > 1:
    for s in sys.argv[1:]:
        l.append(s)
save_to_json_file(l, 'add_item.json')
