#!/usr/bin/python3

'''define Rectangle class'''


class Rectangle:
    '''rectangle  class
    args:
        width: the width of Rectangle
        height: the height of the height
    attributes:
        number_of_instances: keep tracks of How many instances created
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''counts the area of a regtangle and return it'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the rectangle perimeter:'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            if i != self.height - 1:
                rectangle_str += str(Rectangle.print_symbol * self.width + "\n")
            else:
                rectangle_str += str(Rectangle.print_symbol * self.width)
        return rectangle_str

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''called when an instance of Rectangle is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
