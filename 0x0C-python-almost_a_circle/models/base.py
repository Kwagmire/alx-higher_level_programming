#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Almost a circle)

This module defines a base model class.

"""


class Base:
    """Base Model.

    This represents the base of all other classes in this project.

    """

    __nb_objects = 0  #: Number of instantiated bases.

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base

        """
        if id is not None:
            self.id = id  #: This instance's identity
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
