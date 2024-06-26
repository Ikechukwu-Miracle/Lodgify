#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """ The user class inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initializes the user instance """
        super().__init__(*args, *kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def __str__(self):
        """ String representation of the user instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # Example of creating a User instance
if __name__ == "__main__":
    user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
    print(user)
    print(user.to_dict())

