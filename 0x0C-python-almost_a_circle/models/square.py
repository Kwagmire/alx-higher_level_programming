#!/usr/bin/python3
"""Task 12 of ALX Project(Python - Almost a circle)

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

    def update(self, *args, **kwargs):
        """Update the attributes of the Square.

        Args:
            args (list of ints): A list of new values
            kwargs (dict): key/value pairs of new attributes

        """
        if args:
            if len(args) > 1:
                new_args = [None for i in range(len(args) + 1)]
                for index, argument in enumerate(args):
                    if index == 1:
                        new_args[1] = argument
                        new_args[2] = argument
                    elif index >= 2:
                        new_args[index + 1] = argument
                    else:
                        new_args[index] = argument
                    super().update(*new_args, **kwargs)
            else:
                super().update(*args, **kwargs)
        else:
            if "size" in kwargs:
                new_kwargs = kwargs
                new_kwargs["width"] = new_kwargs.get("size")
                new_kwargs["width"] = new_kwargs.get("size")
                del new_kwargs["size"]
                super().update(*args, **new_kwargs)
            else:
                super().update(*args, **kwargs)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
