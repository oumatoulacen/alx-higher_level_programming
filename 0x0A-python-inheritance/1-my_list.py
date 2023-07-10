#!/usr/bin/python3

class MyList(list):
    '''a class MyList that inherits from list'''
    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort)'''
        sorted_list = sorted(self)
        print(sorted_list)
