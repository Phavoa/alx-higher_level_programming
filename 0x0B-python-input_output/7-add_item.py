#!/usr/bin/python3
"""
7-add_item module
"""


import json
from sys import argv
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
aList = []

if os.path.exists(file):
    aList = load_from_json_file(file)

for i in range(1, len(argv)):
    aList.append(argv[i])

save_to_json_file(aList, file)
