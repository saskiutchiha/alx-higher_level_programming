from models.base import Base

class Rectangle(Base):
    """
    Class representing a rectangle.

    Attributes:
    - width (int): Width of the rectangle.
    - height (int): Height of the rectangle.
    - x (int): X-coordinate of the rectangle's position.
    - y (int): Y-coordinate of the rectangle's position.
    - id (int): Unique identifier for the rectangle.

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None): Constructor for the Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the rectangle's position.
        - y (int): Y-coordinate of the rectangle's position.
        - id (int): Unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        value (int): New value for the width.

        Raises:
        TypeError: If the provided value is not an integer.
        ValueError: If the provided value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        value (int): New value for the height.

        Raises:
        TypeError: If the provided value is not an integer.
        ValueError: If the provided value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
        int: X-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Parameters:
        value (int): New value for the x-coordinate.

        Raises:
        TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
        int: Y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Parameters:
        value (int): New value for the y-coordinate.

        Raises:
        TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        self.__y = value
