#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """ This defines all common atributes/methods for other classes """
    def __init__(self):
        """
        Initialize a new instance of the BaseModel.
        - Assigns a unique id to the instance using uuid4 and converts it to a string.
        - Set the created_at attribute to the current time when the instance is cretaed.
        - Set the updated_at attribute as the same value as the created_at attribute.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        def __str__(self):
            """
            Returns the string representation of the instance.
            - Format: [<class name>] (<self.id>) <self.__dict__>.
            """
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            """
            Updated the public instance attribute updated_at with the current datetime.
            This method should be called whenever the instance is modified.
            """
            self.updated_at = datetime.now()

        def to_dict(self):
            """
            Returns a dictionary containg the key/values of __dict__ of the instance
            A value/key __class__is added to the dictionary with the class name of the object.
            Created_at and updated_at are converted to string object using the ISO format that is ISOformat().
            """
            dictionary = self.__dict__.copy()
            dictionary['__class__'] = self.__class__.__name__
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            return dictionary

if __name__ == "__main__":
    base = BaseModel()
    print(base)
    base.save()
    print(base)

