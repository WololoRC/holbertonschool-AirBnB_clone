#!/usr/bin/python
"""Holds State class, inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class
    -----------
    name : str
        empty string by defoult
    """
    name = ""
