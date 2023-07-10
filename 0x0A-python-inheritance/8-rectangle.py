#!/usr/bin/python3
'''Write a class BaseGeometry'''


class BaseGeometry():
    '''BaseGeometry class'''
    def area(self):
        '''aises an Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


'''Write a class Rectangle'''


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
