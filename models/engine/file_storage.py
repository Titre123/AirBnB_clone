#!/usr/bin/python3
'''module - file_storage
serializes instances to a JSON file and deserializes JSON file to instances'''


import json
import os


class FileStorage:
    '''
    This is my class FileStorage
    private instance attribute:
        - file_path
        - objects

    Public instance methods::
        - all
        - new
        - save
        - reload
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''return dictionary __objects in form of BaseModel.id : __str__'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        '''serializes __objects to the JSON file (path)'''
        json_format = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_format)

   def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State
        }
        return classes
