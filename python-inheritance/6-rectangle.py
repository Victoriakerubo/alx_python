#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
