#!/usr/bin/python3
import sys
a = sys.argv
print("{} argument".format(len(a)-1),end="")
i = len(a)-1
if i == 0 :
 print("s.")
else :
    if (i ==1):
     print(":")
    else :
        print("s:")
while(i>0):
 print("{}: {}".format(len(a)-i,a[len(a)-i]))
 i-=1

