# -*- coding: utf-8 -*-
"""Square Module

This module defines a `Square` class that represents a square with a size attribute.
The size attribute is validated to ensure it is an integer and greater than or equal to 0.
The class provides methods for calculating the area of the square and printing the square.

Example:
    You can create an instance of the `Square` class by specifying its size, calculate
    the area of the square, and print the square using the `my_print` method.

Attributes:
    None

Todo:
    * Implement methods for calculating the perimeter and other properties of the square.

"""

class Square:
    """A class to represent a square.

    This class allows you to create a square by specifying its size. The size
    is a private attribute, and this class provides methods for working with
    the square, including calculating the area and printing the square.

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

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using the character #.

        If the size is equal to 0, an empty line is printed.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# Additional documentation for methods, attributes, and functions can be added as needed.

