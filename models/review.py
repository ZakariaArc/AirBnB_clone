#!/usr/bin/python3
"""
it defines the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    it represents a review
    """

    place_id = ""
    user_id = ""
    text = ""
