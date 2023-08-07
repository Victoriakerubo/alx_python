def is_kind_of_class(obj, class_type):
    """Returns True if obj is an instance of class_type or a subclass of class_type."""
    if isinstance(obj, class_type):
        return True
    elif isinstance(obj, type):
        return issubclass(obj, class_type)
    else:
        return False

a = 1

if is_kind_of_class(type(a), int):
    print(f"The integer {a} comes from the int class")
if is_kind_of_class(type(a), float):
    print(f"The integer {a} comes from the float class")
if is_kind_of_class(type(a), object):
    print(f"The integer {a} comes from the object class")

