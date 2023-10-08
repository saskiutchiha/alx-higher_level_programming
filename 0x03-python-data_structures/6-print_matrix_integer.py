#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
 for i in range(len(matrix)):
   for j in range(len(matrix[0])-1):
    print(matrix[i][j],end=" ")
   print(matrix[i][j+1],end="") 
   print("$")
