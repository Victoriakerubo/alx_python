#!/usr/bin/python3

"""This module defines a class named Rectangle that inherits from BaseGeometry.

This module demonstrates inheritance and creating specialized classes.

Example:
    You can create an instance of the Rectangle class and use it to work with
    rectangles. It inherits attributes and methods from BaseGeometry.

    Example usage:

    r = Rectangle(3, 5)
    print(r)
    print(r.area())

Attributes:
    None: This module does not define any module-level attributes.

Todo:
    * Implement the Rectangle class by inheriting from BaseGeometry.
    * Override the area method to calculate the area of the rectangle.
    * Implement a custom __str__ method to provide a rectangle description.

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle is a class for working with rectangles.

    This class inherits attributes and methods from the BaseGeometry class
    and adds attributes and methods specific to rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        The width and height must be positive integers and are validated using
        the integer_validator method inherited from BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """Generate a human-readable string representation of the rectangle.

        Returns:
            str: A string that describes the rectangle in the format "[Rectangle] <width>/<height>"

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

