#!/usr/bin/python3
""" This defines the City Class. """
from models.base_model import BaseModel

class City(BaseModel):
    """ City inherits from BaseModel.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
