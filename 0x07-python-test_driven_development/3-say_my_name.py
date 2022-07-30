#!/usr/bin/python3
"""Task 2 of ALX Project(Python - Test-driven Development)

This module defines the a function that prints a fullname

"""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If either of first_name and last_name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
