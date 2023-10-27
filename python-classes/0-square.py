class Square:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be non-negative")
        else:
            self.__size = new_size

    def __str__(self):
        return f"Square(size={self.__size})"
