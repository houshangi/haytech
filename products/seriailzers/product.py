from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    warehouse = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'category',
                  'description', 'quantity',
                  'price', 'uuid',
                  'warehouse', 'created_date',
                  'image']

    def get_category(self, obj):
        return str(obj.category)

    def get_warehouse(self, obj):
         return str(obj.warehouse)
