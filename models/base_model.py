#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This class is the base model"""

    def __init__(self, *tuble, **dic):
        """Initializes instance attributes

        Args:
            - *tuble: tuble of arguments
            - **dic: dictionary of key-values arguments
        """

        if not dic:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in dic:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        dic["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        dic["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = dic[key]

    def __str__(self):
        """Returns official string representation"""
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)


    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = {}

        for dic_k, res in self.__dict__.items():
            if dic_k == "created_at" or dic_k == "updated_at":
                new_dict[dic_k] = res.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not res:
                    pass
                else:
                    new_dict[dic_k] = res
        new_dict['__class__'] = self.__class__.__name__

        return new_dict