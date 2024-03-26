#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kkargv):
        """initializes all attributes
        """
        if not kkargv:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for dict_k, res in kkargv.items():
                if dict_k == 'created_at' or dict_k == 'updated_at':
                    res = datetime.strptime(kkargv[dict_k], f)
                if dict_k != '__class__':
                    setattr(self, dict_k, res)

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a dict_k and returning
        datemtimes converted to strings
        """
        new_dict = {}

        for dict_k, res in self.__dict__.items():
            if dict_k == "created_at" or dict_k == "updated_at":
                new_dict[dict_k] = res.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not res:
                    pass
                else:
                    new_dict[dict_k] = res
        new_dict['__class__'] = self.__class__.__name__

        return new_dict