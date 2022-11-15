from django.db import models
import uuid
from .product import Product
from rest_framework.authtoken.admin import User


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False
                            )
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE
                              )
    units_ordered = models.PositiveIntegerField()
    total = models.FloatField(default=0.0)

    class Meta:
        permissions = ('add_orders', 'Can Add Orders'),
