#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
         a = 0
         while a < x:
          try:
           print("{:d}".format(my_list[a]))
           a+=1
          except (TypeError, ValueError):
             my_list = my_list[:a] + my_list[a+1:]
             continue  
         return (a)          
