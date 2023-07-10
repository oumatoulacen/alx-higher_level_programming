#!/usr/bin/python3
'''check if an  is an instance of a class that inherited
(directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.'''
    obj_type = type(obj)
    if issubclass(obj_type, a_class) and obj_type != a_class:
        return True
    return False
