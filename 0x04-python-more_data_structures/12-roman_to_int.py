#!/usr/bin/python3
def roman_to_int(roman_string):
   dict = {"I" : 1,	"V":5	,"X":10 ,"L": 50,"C":100,	"D" :500,	"M":1000}
   sum =0;
   for i in range(len(reman_string)-1) :
    
    if dict[reman_string[i]] <  dict[reman_string[i+1]] :
      sum = sum + dict[reman_string[i+1]] - dict[reman_string[i]]
           i+=2
    else :
      sum += dict[reman_string[i]]
   if i == len(reman_string)-2:
     sum += dict[reman_string[i+1]]
   return sum  
