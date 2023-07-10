#!/usr/bin/python3
'''a class MyList that inherits from list'''


class MyList(list):
    '''MyList inherits from list'''
    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort)'''
        s_list = self[:]
        s_list.sort()
        print("{}".format(s_list))
