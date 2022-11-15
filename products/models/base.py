from django.db import models
import uuid


class InfoBase(models.Model):
    """
    Abstract Base Class for Content of All Infos Used in different Entities
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=700,
                                   null=True)
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False
                            )
    image = models.ImageField(null=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
