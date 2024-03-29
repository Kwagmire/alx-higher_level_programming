#!/usr/bin/python3
"""Task 5 of ALX Project(Python - More Classes and Objects)

This module defines a class ``Rectangle``

"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle. Default 0
            height (int): The height of the new rectangle. Default 0

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if any([i == 0 for i in [self.__width, self.__height]]):
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Return the printable representation of the Rectangle

        Represents the rectangle with the # character.
        """
        if any([i == 0 for i in [self.__width, self.__height]]):
            return ""
        else:
            to_print = ""
            for i in range(self.__height):
                if i == self.__height - 1:
                    to_print += "{}".format("#" * self.__width)
                else:
                    to_print += "{}\n".format("#" * self.__width)
            return to_print

    def __repr__(self):
        """Return the string representation of the Rectangle"""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return ret

    def __del__(self):
        """Print a message for every rectangle deleted"""
        print("Bye rectangle...")
