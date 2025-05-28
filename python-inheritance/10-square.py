#!/usr/bin/python3
"""Module that includes a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        super().__init__(size, size)
        self.__size = size
