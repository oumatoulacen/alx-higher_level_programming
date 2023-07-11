#!/usr/bin/python3
'''
Write a class Student that defines a student
'''


class Student:
    '''
    Student class that defines a student by:
        Public instance attributes:
            first_name
            last_name
            age'''
    def __init__(self, first_name, last_name, age):
        '''class instance constractor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance '''
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
