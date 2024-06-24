#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """ City inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initializes City instance """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        """ Returns the string representation of the City Instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
