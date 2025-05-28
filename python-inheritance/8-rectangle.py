#!/usr/bin/python3
"""Module that defines a rectangle class using BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)