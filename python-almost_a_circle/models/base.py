# File: models/base.py

class Base:
    """
    This is the Base class.

    It serves as the base class for all other classes in this project.
    It manages the id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        :param id: An integer representing the id of the instance.
                   If None, __nb_objects is incremented and assigned to the instance id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
