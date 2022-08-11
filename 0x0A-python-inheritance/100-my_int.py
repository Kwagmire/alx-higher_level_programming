#!/usr/bin/python3
"""Task 12 of ALX Project(Python - Inheritance)

This modules define a custom class. one that rebels the `int` class.

"""


class MyInt(int):
    """Initialize a rebel `int` class"""

    def __eq__(self, value):
        return self != value

    def __ne__(self, value):
        return self == value
