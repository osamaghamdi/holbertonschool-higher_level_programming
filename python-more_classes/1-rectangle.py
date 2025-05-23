#!/usr/bin/python3
"""Defines an empty Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

@property
def width(self):
    """
    Get the current width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """
    return self.__width

@width.setter
def width(self, value):
    """
    Set a new width for the rectangle.

    Args:
        value (int): The new width of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@property
def height(self):
    """
    Get the current height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """
    return self.__height

@height.setter
def height(self, value):
    """
    Set a new height for the rectangle.

    Args:
        value (int): The new height of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value