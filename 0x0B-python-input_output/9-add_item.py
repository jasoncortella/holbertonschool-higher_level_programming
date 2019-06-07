#!/usr/bin/python3
"""Script to add all arguments to a Python list, and save to a file"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    jlist = load_from_json_file("add_item.json")
except:
    jlist = []

for arg in sys.argv[1:]:
    jlist.append(arg)

save_to_json_file(jlist, "add_item.json")
