#!/usr/bin/python3
def roman_to_int(roman_string):
   dict = {"I" : 1,	"V":5	,"X":10 ,"L": 50,"C":100,	"D" :500,	"M":1000}
   sum =0
   i=0
   if (roman_string == None) :
      return 0
   while i< len(roman_string) :
    if i == len(roman_string)-1:
      sum += dict[roman_string[i]]
      break
    if dict[roman_string[i]] <  dict[roman_string[i+1]] :
      sum = sum + dict[roman_string[i+1]] - dict[roman_string[i]]
     
      i+=2
    else :
      sum += dict[roman_string[i]]
      i+=1    
   return sum  
