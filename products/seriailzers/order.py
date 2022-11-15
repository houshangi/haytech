from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'owner': {'required': False},
                        'total': {'required': False}}


class OrderDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["uuid",
                  "order_date",
                  "units_ordered",
                  "total", "product",
                  "owner"]

    def get_owner(self,obj):
        return str(obj.owner)

    def get_product(self,obj):
        return str(obj.product)
