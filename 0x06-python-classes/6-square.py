#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0,position=(0,0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not  isinstance(size, int):
         raise TypeError("size must be an integer")
        elif size < 0:
         raise ValueError("size must be >= 0")
        else :
         self.__size = size 
        if (not isinstance(value, tuple)) or len(value) != 2 or (value[0] < 0 or value[1] < 0):
         raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property  
    def position(self):
      """Get/set the current position of the square."""  
      return self.__position
    @position.setter  
    def position(self,value):
        """
        Setter method for the position property.
        Args:
        value (tuple): A tuple representing the new (x, y) position.
        Raises:
        TypeError: If the value is not a tuple of 2 positive integers.
        """ 
        if (not isinstance(value, tuple)) or len(value) != 2 or (value[0] < 0 or value[1] < 0):
         raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character and spases."""
        for i in range(0, self.__size):
            print(" "*(self.position)[0],end="")
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
