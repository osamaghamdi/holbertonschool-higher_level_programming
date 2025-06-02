#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A class that inherits from list and adds a method to print sorted."""
    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))
