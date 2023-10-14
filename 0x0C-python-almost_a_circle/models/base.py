#!/usr/bin/python3

"""Defines the base class"""

class Base:
    """The Base Class
    
    This class will be inherited and modified by other classes.

    Attributs:
        __nb_objects (int): num instances of class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init the Base Class
       
        Args:
            id (int): id of the instances
        """
        
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

        
