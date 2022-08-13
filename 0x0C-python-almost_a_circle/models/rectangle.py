#!/usr/bin/python3
"""Task 2 of ALX Project(Python - Almost a circle)

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

        """
        super().__init__(id)
        self.__width = width  #: width of Rectangle
        self.__height = height  #: height of Rectangle
        self.__x = x  #: x-coordinate of Rectangle
        self.__y = y  #: y-coordinate of Rectangle

    @property
    def width(self):
        """Get/Set the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of a Rectangle"""
        return self.__height

    @height.setter
    def width(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/Set the x-coordinate of a Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/Set the y-coordinate of a Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
