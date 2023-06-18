#!/usr/bin/python3

def uniq_add(my_list=[]):
    j = 0
    for i in list(set(my_list)):
        j += i
    return j
