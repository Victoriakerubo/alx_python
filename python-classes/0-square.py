def __init__(self, size):
    self.__size = int(size)

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size * self.__size


if __name__ == "__main__":
    square = Square(3)
    print(square.size)
