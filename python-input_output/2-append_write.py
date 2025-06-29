#!/usr/bin/python3
"""Define a file appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
