
class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Args:
            id (int, optional): id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

