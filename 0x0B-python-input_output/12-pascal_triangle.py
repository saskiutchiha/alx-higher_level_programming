#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    - list of lists: A list of lists representing Pascal's Triangle up to the nth row.
      Each inner list corresponds to a row in the triangle.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    l = [[1]]
    if n <= 0 :
        return []

    for i in range(1,n):
        l = l + [l[i-1] + [1]]
        j = i-1
        while j > 0:
            l[i][j] = l[i][j] + l[i][j-1]
            j-=1
    return l
