#!/usr/bin/python3
"""Module for FileStorage class."""


import datetime
import json
import os
script_dir = os.path.dirname(__file__)


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = os.path.join(script_dir, "file.json")
    __objects = {}

    def all(self):
        ''' return FileStorage.__objects '''
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = key = str(type(obj).__name__) + '.' + str(obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Serialzes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

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
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects.clear()
            FileStorage.__objects.update(obj_dict)
