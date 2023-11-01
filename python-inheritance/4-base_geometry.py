# -*- coding: utf-8 -*-
"""This module defines a simple class named BaseGeometry.

This module demonstrates documentation using Google-style docstrings.

Example:
    You can create an instance of the BaseGeometry class and use it to work
    with basic geometry operations.

    Example usage:

    bg = BaseGeometry()
    result = bg.area()  # Replace 'area' with a method name you intend to define.
    print(result)

Attributes:
    None: This module does not define any module-level attributes.

Todo:
    * Define methods for geometry operations.
    * Implement additional functionality for the BaseGeometry class.

"""

class BaseGeometry:
    """BaseGeometry is a class for basic geometry operations.

    This class can be used as a base for more specialized geometry classes.
    You should implement geometry-related methods in your derived classes.

    Attributes:
        None: This class does not define any attributes by default.

    """

    def area(self):
        """Calculate the area of the geometry.

        You should implement this method in your derived classes.

        Returns:
            float: The calculated area.

        Raises:
            Exception: This method raises an Exception with the message
                "area() is not implemented" to indicate that it should be
                implemented in the derived classes.

        """
        raise Exception("area() is not implemented")

    def perimeter(self):
        """Calculate the perimeter of the geometry.

        You should implement this method in your derived classes.

        Returns:
            float: The calculated perimeter.

        Raises:
            Exception: This method raises an Exception with the message
                "perimeter() is not implemented" to indicate that it should be
                implemented in the derived classes.

        """
        raise Exception("perimeter() is not implemented")

