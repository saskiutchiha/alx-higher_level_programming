#!/usr/bin/python3
""" print_square prints a square depending on the "size" parameter
"""
def print_square(size):
    """ Prints a square with a size
    checks if "size" is an int
    checks if "size" is a float and less than 0
    checks if "size" is less than 0
    checks if "size" is equal to 0
    """
    if not isinstance(size,int):
        raise TypeError("size must be an integer")
    elif size < 0 :
        raise ValueError("size must be >= 0")
    else :
        for i in range(size):
            for j in range(size):
                print("#",end="")
            print("")
            
