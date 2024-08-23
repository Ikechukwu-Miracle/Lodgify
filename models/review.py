#!/use/bin/python3
""" This defines the Review Class. """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class inherits from BaseModel.
    Attributes:
        place_id (str): THe Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
