#!/usr/bin/python3
"""Module that includes a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
    
    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
