#!/usr/bin/python3
''' module - city
This is the city model for my application'''


from models.base_model import BaseModel


class City(BaseModel):
    '''
    BaseModel Inherited
    Public class attributes:
        - state_id
        - name
    '''
    state_id = ""
    name = ""
