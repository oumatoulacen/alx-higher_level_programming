#!/usr/bin/python3

'''define Rectangle class'''


class Rectangle:
    '''rectangle  class
    args:
        width: the width of Rectangle
        height: the height of the height
    '''
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    '''get/set width'''
    @property
    def width(self):
        """ Getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets the height"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    '''get/set heght'''
    @property
    def height(self):
        """ Getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets the  height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
