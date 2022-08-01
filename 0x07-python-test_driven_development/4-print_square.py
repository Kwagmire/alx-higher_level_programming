#!/usr/bin/python3
"""Task 3 of ALX Project(Python - Test-driven Development)

This module defines a function that prints a square

"""


def print_square(size):
    """Print a square of size ``size``

    Args:
        size (int): The size of the square

    Raises:
        TypeError: if size is not an integer
            if size is not specified
        ValueError: if size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#" * size) for i in range(size)]
