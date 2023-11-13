#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""
def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """
    
    matrix2 = [line[:] for line in matrix]
    l = len(matrix[0])
    x,y = 0,0
    for line_matrix in matrix2:
        if len(line_matrix) != l:
            raise TypeError("Each row of the matrix must have the same size")
        y = 0

        for j in line_matrix:
            if not (isinstance(j,int) or isinstance(j,float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else :
                 if not (isinstance(div,int) or isinstance(div,float)):
                     raise TypeError("div must be a number")
                 elif div == 0 :
                     raise ZeroDivisionError("division by zero")
                 else :
                     matrix2[x][y] =  round( matrix[x][y] / div,2)
            y+=1
        x+=1
    
    return matrix2
