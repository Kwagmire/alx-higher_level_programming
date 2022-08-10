#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Inheritance)

This modules defines a class that inherits from ``list``.

"""


class MyList(list):
    """Implements sorted priting for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
