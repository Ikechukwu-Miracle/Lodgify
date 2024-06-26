#!/usr/bin/python3
"""Define the BaseModel class"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents the BaseModel"""
    
    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel object"""
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_fmt)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Return the str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return f'[{clsname}] ({self.id}) {self.__dict__}'
    
    def save(self) -> None:
        """Update the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self) -> dict:
        """Return a dictionary containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic