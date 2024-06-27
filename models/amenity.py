#!/usr/bin/python3
""" THis defines the Amenity Class """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity inherits from BaseModel.
    Attributes:
        name (str): The name of the Amenity.
    """

    name = ""
