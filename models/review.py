#!/use/bin/python3

from models.basemodel import BaseModel

class Review(BAseModel):
    """ Review class inherits from BaseModel """
    def __init__(self, *args, *kwargs):
        """ Initializing the review instance """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

    def __str__(self):
        """ The string representation of the Review instance. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
