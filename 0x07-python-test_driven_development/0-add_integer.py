#!/usr/bin/python3
"""Task 0 of ALX Project(Python - Test-driven development)

This module defines a function that adds two integers

"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int): the first number
        b (int, optional): the second number, defaults to 98

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if any of a and b isn't an integer or a float

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
