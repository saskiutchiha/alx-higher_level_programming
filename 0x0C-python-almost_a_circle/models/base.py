#!/usr/bin/python3
class Base :
    __nb_objects = 0
    def __init__(self,id=None):
        if (id != None):
            self.id = id
        else:
            base.__nb_objects+=1
            self.id = base.__nb_objects 

