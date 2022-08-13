#!/usr/bin/python3
"""Task 6 of ALX Project(Python - Almost a circle)

This module defines a rectangle class.

"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle.

    Rectangle is based on the base model class.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): Its height.
            x (int): (Optional) Its position on the x-axis.
            y (int): (Optional) Its position on the y-axis.
            id (int): (Optional) Its identity

        Raises:
            TypeError: if any of the values is not an integer.
            ValueError: if `width` or `height` is less than 1.
                        if `x` or `y` is less than 0.

        """
        super().__init__(id)
        self.width = width  #: width of Rectangle
        self.height = height  #: height of Rectangle
        self.x = x  #: x-coordinate of Rectangle
        self.y = y  #: y-coordinate of Rectangle

    @property
    def width(self):
        """Get/Set the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/Set the x-coordinate of a Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/Set the y-coordinate of a Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle with the character ``#``"""
        (print() for i in range(self.y))
        print("{}{}\n".format(" " * self.x, "#" * self.__width)
              * self.__height, end="")

    def __str__(self):
        """Return the string representation of a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
