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

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        '''return the area of a rectangle'''
        return self.__width * self.__height
