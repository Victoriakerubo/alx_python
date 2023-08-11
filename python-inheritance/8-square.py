#!/usr/bin/python3

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call parent constructor to set width and height

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[Square] {}/{}".format(self.width, self.height)  # Use getter methods

# Rest of your code for testing
