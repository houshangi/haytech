from django.db import models
from .category import Category
from .base import InfoBase
from .warehouse import WareHouse


class Product(InfoBase):
    """
    model class  for Products
    this class is Inhrited from MetaDataBaseClass
    """
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 )
    warehouse = models.ForeignKey(WareHouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()  # in a real World Scenario this must be a float !

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_products', 'Can View Products'),
            ('change_products', 'Can Change Products'),
            ('add_products', 'Can Add Products'),
            ('delete_products', 'Can Delete Products'),
        )
