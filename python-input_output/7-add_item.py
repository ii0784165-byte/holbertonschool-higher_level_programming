#!/usr/bin/python3
'''nese'''


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# If file exists → load list, otherwise start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (converted to strings)
items.extend(sys.argv[1:])

# Save updated list back to JSON file
save_to_json_file(items, filename)
