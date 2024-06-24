#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initializes amenity instance """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        """ Retrns String representation of Amenity Instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
