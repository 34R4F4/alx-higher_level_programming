#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__height + self.__width) if self.__height != 0 and self.__width != 0 else 0
