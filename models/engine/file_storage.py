#!/usr/bin/python3
""" module defining a class for managing  storage"""
import json


class FileStorage:
    """ managing storage of airbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dict of models """
        return FileStorage.__objects

    def reload(self):
        """Loads storage dictionary from any file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            holder = {}
            with open(FileStorage.__file_path, 'r') as f:
                holder = json.load(f)
                for dict_k, res in holder.items():
                    self.all()[dict_k] = classes[res['__class__']](**res)
        except FileNotFoundError:
            pass

    def save(self):
        """Saves storage dict to file"""
        with open(FileStorage.__file_path, 'w') as file:
            holder = {}
            holder.update(FileStorage.__objects)
            for dict_k, res in holder.items():
                holder[dict_k] = res.to_dict()
            json.dump(holder, file)

    def new(self, obj):
        """Adding new object to dict"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
