#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __eq__(self, other):
        """what was != is now =="""
        return not self - other == 0

    
    def __ne__(self, other):
        """what was == is now !="""
        return not self - other != 0
