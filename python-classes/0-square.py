class Square:
    """Represents a square.

    Attributes:
        size: The size of the square.
    """

    def __init__(self, size):
        """Initializes a new square with the given size.

        Args:
            size: The size of the square. Must be an integer greater than or equal to zero.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be non-negative")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Sets the size of the square.

        Args:
            new_size: The new size of the square. Must be an integer greater than or equal to zero.
        """

        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be non-negative")
        else:
            self.__size = new_size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"Square(size={self.__size})"

