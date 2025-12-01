#!/usr/bin/python3
"""hello man """


def write_file(filename="", text=""):
    '''you ehats up'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
