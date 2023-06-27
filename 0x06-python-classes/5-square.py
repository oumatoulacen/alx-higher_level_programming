#!/usr/bin/python3
"""define a class"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize a square
        args:
            size: the size of new square
        """
        self.size = size

    """get size"""
    @property
    def size(self):
        return self.__size

    """set size"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """count area of a square"""

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
