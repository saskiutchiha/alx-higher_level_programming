#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    while a < x:
        try :
            print(my_list[a],end="")
        except:
            
            break
        a+=1
    if (a<=x):
        print("") 
    return a      
