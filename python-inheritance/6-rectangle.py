# File: 6-rectangle.py

class BaseGeometry:
    """
    This is the BaseGeometry class.

    It serves as the base class for geometry-related operations.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        This method raises an exception indicating that it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method to validate an integer value.

        :param name: A string representing the name of the value to validate.
        :param value: The value to be validated.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class, inheriting from BaseGeometry.

    It represents a rectangle with width and height attributes.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        :return: A string representing the rectangle's dimensions.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

