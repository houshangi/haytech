from rest_framework import permissions
from django.conf import settings


class CustomerAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.groups.\
            filter(name__in=[settings.CUSTOMER_GROUP_NAME])\
            .exists()
