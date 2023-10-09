#!/usr/bin/python3

class Square:
    """This is a Square class."""

    def __init__(self, size):
        """Initialize a Square instance with a given size."""
        self.__size = size

mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

try:
    print(mysquare.size)
except Exception as e:
    print(e)

try:
    print(mysquare._Square__size)
except Exception as e:
    print(e)


