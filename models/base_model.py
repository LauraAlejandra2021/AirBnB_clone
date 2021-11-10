#!/usr/bin/python3
"""this module create the class call BaseModel"""
from datetime import date, datetime
from uuid import uuid4


class BaseModel:
    """A class BaseModel
    Attributes"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):

        """Return a string of the class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""

        self.update_at = datetime.now()

    def to_dict(self)
        """returns a dictionary containing all keys/values"""

        new = self.__dict__.copy()
        new['__class__'] = self.__class__.__name__
        new['created_at'] = datetime.isoformat(new['created_ad'])
        new['updated_at'] = datetime.isoformat(new['updated_at'])
        return new