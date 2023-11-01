#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""Module to check if an object inherits from a specified class.

This module provides a function, `inherits_from`, that checks if an object is an instance of a class that
inherited (directly or indirectly) from the specified class.

Example:
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

Attributes:
    None

Todo:
    * None

"""

def inherits_from(obj, a_class):
    """Check if the object inherits from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if `obj` is an instance of a subclass that inherits from `a_class`, False otherwise.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class


