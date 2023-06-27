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
