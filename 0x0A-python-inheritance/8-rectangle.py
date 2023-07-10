#!/usr/bin/python3
"""Geometry module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

'''Write a class Rectangle'''


class Rectangle(BaseGeometry):
    """
    A class inherits the BaseGeometry class
    Private instance attributes:
        -width
        -height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
