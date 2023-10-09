#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  verif = []
  for i in my_list :
   if i%2 == 0:
    verif += [True]
   else :
    verif += [False]
  return verif
