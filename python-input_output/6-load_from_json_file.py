#!/usr/bin/python3
'''nese'''


import json


def load_from_json_file(filename):
    '''iqrayu'''
    with open(filename, "r") as f:
        return json.load(f)
