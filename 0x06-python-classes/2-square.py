#!/usr/bin/python3

"""define a class"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize a square
        args:
            size: the size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
