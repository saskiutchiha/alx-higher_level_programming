#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        if len(my_list) == 1 :
            print("{:d}".format(my_list[0]))
        else :    
         print_reversed_list_integer(my_list[1:])
         print("{:d}".format(my_list[0]))
