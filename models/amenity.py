#!/usr/bin/bash
''' module - amenity
This is the amenity model for my application'''


from base_model import BaseModel


class Amenity(BaseModel):
    '''
    BaseModel Inherited

    Public class attributes:
        - name
    '''
    name = ""
