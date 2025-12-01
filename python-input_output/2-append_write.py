#!/usr/bin/python3
'''yoooooo lets goooooooooo'''


def append_write(filename="", text=""):
    '''nice to meet you'''
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
