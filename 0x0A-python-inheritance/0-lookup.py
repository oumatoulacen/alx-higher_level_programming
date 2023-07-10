#!/usr/bin/python3
"""
Finding a list of available attributes and methods of an object
"""

def lookup(obj):
    '''lists all the attributes and methods of an object'''
    return sorted(dir(obj))
