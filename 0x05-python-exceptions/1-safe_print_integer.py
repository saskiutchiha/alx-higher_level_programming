#!/usr/bin/python3
def print_safe(value):
   try :
    print("{:d}\n".format(value))
    return True
   except Exception :
      return False
