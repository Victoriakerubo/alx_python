# -*- coding: utf-8 -*-
"""This module defines a class named BaseGeometry.

This module demonstrates documentation using Google-style docstrings.

Example:
    You can create an instance of the BaseGeometry class and use it to work
    with basic geometry operations.

    Example usage:

    bg = BaseGeometry()
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

Attributes:
    None: This module does not define any module-level attributes.

Todo:
    * Implement the 'area' and 'perimeter' methods.
    * Implement the 'integer_validator' method to validate integer values.

"""

class BaseGeometry:
    """BaseGeometry is a class for basic geometry operations.

    This class can be used as a base for more specialized geometry classes.

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

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Returns:
            None: This method does not return a value.

        Raises:
            TypeError: If 'value' is not an integer, this method raises a
                TypeError exception with the message "<name> must be an integer."
            ValueError: If 'value' is less than or equal to 0, this method raises
                a ValueError exception with the message "<name> must be greater than 0."

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

