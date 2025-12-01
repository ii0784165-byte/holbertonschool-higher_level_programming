#!/usr/bin/python3
''' yo yoy oy whats up nigga '''


import json


def save_to_json_file(my_obj, filename):
    ''' ne poymat i poteryat '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
