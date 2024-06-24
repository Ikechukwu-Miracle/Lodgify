#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """ Place inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Intializes the Place Instance """
        super().__init__(*args, **kwargs)
        self.city_id = Kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])


    def __str__(self):
        """ Returns the string representation of Place Instanc """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"