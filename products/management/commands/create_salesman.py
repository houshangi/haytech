"""
Create permission groups
Create permissions  to models for a set of groups(if needed)
"""
import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.conf import settings

GROUPS = [settings.SALESMAN_GROUP_NAME]
MODELS = ['products', "warehouse"]
PERMISSIONS = ['Can View Products',
               'Can Change Products',
               'Can Add Products',
               'Can Delete Products']


class Command(BaseCommand):

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                for permission in PERMISSIONS:
                    try:
                        model_add_perm = Permission.objects.get(name=permission)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(permission))
                        continue

                    new_group.permissions.add(model_add_perm)
