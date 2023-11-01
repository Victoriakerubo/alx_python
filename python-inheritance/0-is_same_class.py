# -*- coding: utf-8 -*-
"""A module for checking if an object is an instance of a specified class.

This module provides a function to determine whether an object is exactly an
instance of a specified class. It can be used to check if an object belongs to
a particular class or its subclasses.

Example:
    The module can be used to check if an object 'a' is an instance of the 'int' class:
    
    >>> a = 1
    >>> is_same_class(a, int)
    True

Attributes:
    None

Todo:
    None
"""

def is_same_class(obj, a_class):
    """Check if the object is an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class, False otherwise.

    Example:
        >>> a = 1
        >>> is_same_class(a, int)
        True

    >>> a = 'Hello'
    >>> is_same_class(a, int)
    False
    """

    return type(obj) == a_class

