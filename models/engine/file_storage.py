#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        # TODO: should this be a copy()?
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = key = str(type(obj).__name__) + '.' + str(obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        '''serializes __objects to the JSON file (path)'''
        json_format = json.dumps(d = {k: v.to_dict() for k, v in FileStorage.__objects.items()})
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_format)

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

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
           dict = json.load(f)
           dict = {key: self.classes()[value["__class__"]](**v)
                        for key, value in dict.items()}
            FileStorage.__objects = dict
