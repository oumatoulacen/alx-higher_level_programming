#!/usr/bin/python3

def lookup(obj):
    '''lists all the attributes and methods of an object'''
    return sorted(dir(obj))
