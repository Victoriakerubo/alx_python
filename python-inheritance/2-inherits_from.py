#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
