#!/usr/bin/python3
''' module - place
This is the place model for my application'''


from base_model import BaseModel


class Review(BaseModel):
    '''
    BaseModel Inherited
    Public class attributes:
        - place_id
        - user_id
        - text
    '''
    place_id = ""
    user_id = ""
    text = ""
