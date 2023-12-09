#!/usr/bin/python3
"""
it defines the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    it represents a User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
