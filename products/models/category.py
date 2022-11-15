from django.db import models
from .base import InfoBase


class Category(InfoBase):
    """
    this class is inherited from MetaDataBaseClass.
    """
    def __str__(self):
        return self.name
