# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models import Category, Product
from products.seriailzers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from ..permissions import SalesManAccessPermission


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [SalesManAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', 'description', 'created_date', 'uuid']


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [SalesManAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
