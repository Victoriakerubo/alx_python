inherits_from = __import__('2-inherits_from').inherits_from

a = 1
if inherits_from(a, int):
    print("{} comes from {}".format(a, int.__name__))
if inherits_from(a, float):
    print("{} comes from {}".format(a, float.__name__))
if inherits_from(a, object):
    print("{} comes from {}".format(a, object.__name__))