from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from products.models import Category


class SalesAPITest(TestCase):

    def _create_super_user(self):
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    def _login_and_retrieve_token_by_admin(self):
        data = {"username": "admin",
                "password": "admin"}  # passwords should get encoded outside of unit tests !!!!
        content_type = "application/json"
        response = self.client.post('/api-token-auth/',
                                    data=data,
                                    content_type=content_type)
        return response.data['token']

    def test_create_category_by_admin(self):
        self._create_super_user()
        token = self._login_and_retrieve_token_by_admin()
        content_type = "application/json"
        data = {"name": "sport",
                "description": "its a category for sporst"}
        response = self.client.post("/api/v1/products/category",
                                    content_type=content_type,
                                    data = data ,
                                    **{"HTTP_AUTHORIZATION": f"Token {token}"}
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



