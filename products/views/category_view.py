from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from products.models import Category, Product
from products.seriailzers import CategorySerializer, ProductSerializer
import django_filters.rest_framework


class CategoryAPIView(ListCreateAPIView):
    """
    it was Specified in requirement Document that only admin Can make Category
    **** pagination is Confined Generally in settings.py ****
    """
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', 'description', 'created_date', 'uuid']


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', 'description', 'created_date', 'uuid']
