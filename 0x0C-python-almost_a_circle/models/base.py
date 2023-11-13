#!/usr/bin/python3
""" define the classe """

class Base :
    __nb_objects = 0
    def __init__(self,id=None):
        """ initialse id of object"""
        if (id != None):
            self.id = id
        else:
            base.__nb_objects+=1
            self.id = base.__nb_objects 

