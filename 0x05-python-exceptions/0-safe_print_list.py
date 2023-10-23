#usr/bin/python3
def safe_print_list(my_list=[], x=0):
  a = 0
  for i in my_list:
    if (a<x):
     try :
       print(i,end="")
     except :
       print("\n")
    a+=1
  print("")
  return a  
