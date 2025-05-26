#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):

    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(int(i) for i in self))