#!/usr/bin/python3
def print_safe(val):
   try :
    print("{:d}".format(val))
    return True
   except Exception :
      return False
