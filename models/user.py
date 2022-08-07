#!/usr/bin/bash
''' module - user
This is the user model for my application'''


from base_model import BaseModel


class User(BaseModel):
    '''
    BaseModel Inherited
    Public class attributes:
        - email
        - password
        - first_name
        - last_name
        '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
