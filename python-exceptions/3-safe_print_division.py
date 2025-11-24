#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print('{:d} / {:d} = {}'.format(a, b, a/b)
        return True
    except ZeroDivisionError:
        return None
