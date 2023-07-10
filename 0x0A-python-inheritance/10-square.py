#!/usr/bin/python3
''' Rectangle module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square class which inherits from Rectangle
    Private instance attributes:
        -size
    '''
    def __init__(self, size):
        '''Square constractor'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''counts the area of a square'''
        return self.__size * self.__size
