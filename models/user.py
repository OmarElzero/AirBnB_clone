#!/usr/bin/python3
""" module to detrmine a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class for  defining a new user by many attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
