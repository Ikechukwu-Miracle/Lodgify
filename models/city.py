#!/usr/bin/python3

import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from models.base_model import BaseModel

class City(BaseModel):
    """ City inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initializes City instance """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')

    def __str__(self):
        """ Returns the string representation of the City Instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

if __name__ == "__main__":
    city = City(state_id="state_123", name="Nigeria")
    print(city)
    print(city.to_dict())
