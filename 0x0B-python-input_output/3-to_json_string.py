#!/usr/bin/python3
'''Write a function that returns the JSON
representation of an object (string)'''


import json
'''the json module'''


def to_json_string(my_obj):
    '''returns the JSON representation of an object (string)'''
    return json.dumps(my_obj)
