#!/usr/bin/python3
""" City Module """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class to get the state id and the name """
    state_id = ""
    name = ""
