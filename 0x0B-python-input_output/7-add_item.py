#!/usr/bin/python3
"""
7-add_item module
"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
ag = sys.argv
json_list = []

if os.path.isfile(filename):
    json_list = load_from_json_file(filename)

for i in range(1, len(ag)):
    json_list.append(ag[i])

save_to_json_file(json_list, filename)
