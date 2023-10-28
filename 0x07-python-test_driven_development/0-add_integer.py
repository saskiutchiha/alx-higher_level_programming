#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>> add_integer(2,5)
    7
    """
    if isinstance(a,int) or isinstance(a,float):
        if isinstance(b,int) or isinstance(b,float):
           return int(a) + int(b)
        else :
            raise TypeError("b must be integer")
    else :
          raise  TypeError("a must be integer")
   # try :
     #   z = a+b
    #    return int(z)
   # except TypeError :
       # if not isinstance(a,int):
      #   print("a must be integer")
     #   if not isinstance(b,int):
    #        print("b must be integer")
   # finally :
  #      return 


