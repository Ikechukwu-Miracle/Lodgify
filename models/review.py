#!/use/bin/python3
""" This defines the Review Class. """
from models.basemodel import BaseModel

class Review(BAseModel):
    """ Review class inherits from BaseModel.
    Attributes:
        place_id (str): THe Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""`
