# -*- coding: utf-8 -*-
"""Rectangle Module

This module defines the `Rectangle` class, which inherits from `BaseGeometry` and represents a geometric rectangle.

Attributes:
    module_level_variable1 (int): Example module-level variable.
    module_level_variable2 (int): Another example module-level variable.

"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class for representing rectangles.

    This class inherits from BaseGeometry and adds specific functionality for rectangles.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        # Validate and set width and height using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Set private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


