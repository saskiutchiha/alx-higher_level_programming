#!/usr/bin/python3
if __name__ == "__main__" :

     import sys
     a = sys.argv
     sum =0
     for j in range(1,len(a)):
            sum += int(a[j])
     print(sum) 
