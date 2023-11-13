#!/usr/bin/python3
""" define the classe """

class Base:
     """ initialse id of object"""
    __nb_objects = 0
    def __init__(self,id=None):
        """ initialse id of object"""
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects 

