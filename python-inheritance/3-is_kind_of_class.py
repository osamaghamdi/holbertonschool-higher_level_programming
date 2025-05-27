#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if it is an instance of a class that inherited from, a specified class."""
    if isinstance(obj, a_class):
        return True
    return False
