#!/usr/bin/python3
"""Task 10 of ALX Project(Python - Almost a circle)

This module defines a `Square` class.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

        Args:
            size (int): The length of the square
            x (int): (Optional) Its x-coordinate
            y (int): (Optional) Its y-coordinate
            id (int): (Optional) Its identity

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/Set the length of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
