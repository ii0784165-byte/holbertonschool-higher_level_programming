#!/usr/bin/python3
"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class
    or an instance of a class that inherited from a_class.
    Otherwise, returns False.
    """
    return isinstance(obj, a_class)
