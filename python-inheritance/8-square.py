#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""Square Module

This module defines the `Square` class, which inherits from `Rectangle` and represents a geometric square.

"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """A class for representing squares.

    This class inherits from Rectangle and adds specific functionality for squares.

    """

    def __init__(self, size):
        """Initialize a Square instance with the given size.

        Args:
            size (int): The size of the square.

        """
        # Call the constructor of the parent class (Rectangle) with size for both width and height
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>".

        """
        return "[Square] {}/{}".format(self.__width, self.__height)

