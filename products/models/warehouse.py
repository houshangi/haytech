from django.db import models
import uuid


class WareHouse(models.Model):
    name = models.CharField(max_length=50)
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_warehose', 'Can View Warehouse'),
            ('change_warehose', 'Can Change Warehouse'),
            ('add_warehose', 'Can Add Warehouse'),
            ('delete_warehose', 'Can Delete Warehouse'),
        )
