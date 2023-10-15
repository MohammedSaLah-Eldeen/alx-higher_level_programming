#!/usr/bin/python3
"""Defines the base class"""

import json

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


    @staticmethod
    def to_json_string(list_dictionaries):
        """creates a json representation of the passed"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    
    @classmethod
    def save_to_file(cls, list_objs):
        """serializes objects to a file"""
        filen = cls.__name__ + ".json"           

        with open(filen, "w") as jsonf:
            if list_objs is None:
                jsonf.write("")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                jsontxt = Base.to_json_string(list_dictionaries)
                jsonf.write(jsontxt)

    @staticmethod
    def from_json_string(json_string):
        """helper function to convert json to py objects"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method to create an instance"""
        if cls.__name__ == "Rectangle":
            tmp = cls(2, 3)
        elif cls.__name__ == "Square":
            tmp = cls(2)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """deserializes json to their respective objects"""
        filen = cls.__name__ + ".json"
        try:
            with open(filen, "r") as jsonf:
                content = jsonf.read()
                list_dictionaries = Base.from_json_string(content)
                list_objs = [cls.create(**dictionary) for dictionary in list_dictionaries]
                return list_objs
            
        except FileNotFoundError:
            return []
