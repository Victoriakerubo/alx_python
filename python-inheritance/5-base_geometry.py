#!/usr/bin/python3

class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        """
        Calculates the area.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
