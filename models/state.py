#!/usr/bin/python3
from .base_model import BaseModel

class State(BaseModel):
    """
    State class inherits from BaseModel.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the state instance.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        """
        Returns the string representation of state instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

