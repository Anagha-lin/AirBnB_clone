#!/usr/bin/python3
"""Implementation of the BaseModel class."""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """A base class for other models, providing common functionality."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            args: Additional positional arguments (not used).
            kwargs: Keyword arguments to initialize the object.

        Attributes:
            id (str): A unique identifier generated using uuid4.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
        """
        self.id = kwargs.get('id', str(uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', self.created_at)

        if kwargs:
            for key, value in kwargs.items():
                if key not in {'id', 'created_at', 'updated_at', '__class__'}:
                    if key in {'created_at', 'updated_at'}:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

        else:
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel.

        Returns:
            str: A formatted string containing the class name and object details.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' attribute and save the object.

        Updates the 'updated_at' attribute with the current datetime
        and triggers the save operation to persist the object.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert the BaseModel object to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel object.
        """
        obj_dict = {key: value for key, value in self.__dict__.items()
                    if key not in {'created_at', 'updated_at'}}

        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

