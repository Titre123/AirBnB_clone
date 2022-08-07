#!/usr/bin/python3
''' module - base_model
This is the base model for my application'''


import uuid
from datetime import datetime
from models import storage
myuuid = str(uuid.uuid4())
current_time = (datetime.now())


class BaseModel:
    '''This is my class BaseModel
    public instance attribute:
        - id

    Public instance method:
        - save
        - to_dict
    '''
    def __init__(self):
        '''Instantiate instance attributes'''
        self.id = myuuid
        self.created_at = current_time
        self.updated_at = current_time    
    def __str__(self):
        '''string representation of an instance of the class'''
        return f"[{type(self).__name__}] ({self.id}) <{self.__dict__}>"
    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of
        the instance'''
        my_dictionary = self.__dict__
        my_dictionary['created_at'] = datetime.now().isoformat()
        my_dictionary['updated_at'] = datetime.now().isoformat()
        my_dictionary['__class__'] = type(self).__name__

        return my_dictionary
