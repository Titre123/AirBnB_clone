#!/usr/bin/python3
''' module - base_model
This is the base model for my application'''


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''This is my class BaseModel
    public instance attribute:
        - id

    Public instance method:
        - save
        - to_dict
    '''

    def __init__(self, *args, **kwargs):
        '''Instantiate instance attributes'''
        if kwargs:
            del(kwargs['__class__'])
            for (key, value) in kwargs.items():
                self.__setattr__(key, value)
        else:
            self.id = myuuid
            self.created_at = str(uuid.uuid4())
            storage.new(self) = datetime.now())

    def __str__(self):
        '''string representation of an instance of the class'''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of
        the instance'''
        my_dictionary = self.__dict__.copy()
        my_dictionary['created_at'] = datetime.now().isoformat()
        my_dictionary['updated_at'] = datetime.now().isoformat()
        my_dictionary['__class__'] = type(self).__name__

        return my_dictionary
