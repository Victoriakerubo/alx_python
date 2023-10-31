# -*- coding: utf-8 -*-
"""Square Module

This module defines a `Square` class that represents a square with a size attribute.
The size attribute is validated to ensure it is an integer and greater than or equal to 0. 
The class also provides a method for calculating the area of the square.

Example:
    You can create an instance of the `Square` class by specifying its size and calculate
    the area of the square.

Attributes:
    None

Todo:
    * Implement methods for calculating the perimeter and other properties of the square.

"""

class Square:
    """A class to represent a square.

    This class allows you to create a square by specifying its size. The size
    is a private attribute, and this class provides methods for working with
    the square.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """Initialize a Square with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).

        """
        return self.__size ** 2

# Additional documentation for methods, attributes, and functions can be added as needed.

