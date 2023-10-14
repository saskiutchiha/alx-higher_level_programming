#!/usr/bin/python3
# Author -Bamidele Adefolaju
i = 0
for c in range(ord('z') ,ord('a')-1,-1):
   if c%2 == 0: 
    print("{}".format(chr(c)), end="")
   else :
       print("{}".format(chr(c-32)), end="")
