#!/usr/bin/python3

"""
add_integer:
Checks if parameters are int
Returns sum of parameters
"""
def add_integer(a, b=98):
   
    """
    Checks if int, otherwise return sum
    """
    
    if isinstance(a,int) or isinstance(a,float):
        if isinstance(b,int) or isinstance(b,float):
           return int(a) + int(b)
        else :
            raise TypeError("b must be an integer")
    else :
          raise  TypeError("a must be an integer")
   
