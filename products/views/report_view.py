import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from ..models import Product, Order
from .order_view import OrderSerializer
from rest_framework.response import Response
from ..permissions import CustomerAccessPermission
from django.db.models import Sum


class CustomerOrderReportView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [CustomerAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['product__uuid',
                        'order_date', 'units_ordered',
                        'product__warehouse__uuid',
                        'product__name', 'total']

    def get_queryset(self):
        user_orders = Order.objects.filter(owner=self.request.user.id)
        return user_orders


class AdminOrderReportView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['product__uuid',
                        'order_date', 'units_ordered',
                        'product__warehouse__uuid',
                        'product__name', 'total']

    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id')
        user_orders = Order.objects.filter(owner=customer_id)
        return user_orders


class AdminReportTotalView(GenericAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self):
        customer_id = self.request.query_params.get("customer_id", None)
        from_date = self.request.query_params.get("from_date", None)
        to_date = self.request.query_params.get("to_date", None)
        warehouse_uuid = self.request.query_params.get("warehouse_uuid", None)
        customer_orders = Order.objects.filter(owner_id=int(customer_id))
        if from_date:
            customer_orders = customer_orders.filter(order_date__gte=from_date)
        if to_date:
            customer_orders = customer_orders.filter(order_date__lte=to_date)
        if warehouse_uuid:
            customer_orders = customer_orders.filter(product__warehouse__uuid=warehouse_uuid)

        total_units_orders = customer_orders.aggregate(Sum('units_ordered'))
        total_ordered_price = customer_orders.aggregate(Sum('total'))

        data = {"total_units_orders": total_units_orders,
                "total_ordered_price": total_ordered_price}

        return Response(json.dumps(data))


class CustomerReportTotalView(GenericAPIView):
    permission_classes = [CustomerAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self):
        customer_id = self.request.user.id
        from_date = self.request.query_params.get("from_date", None)
        to_date = self.request.query_params.get("to_date", None)
        warehouse_uuid = self.request.query_params.get("warehouse_uuid", None)
        customer_orders = Order.objects.filter(owner_id=customer_id)

        if from_date:
            customer_orders = customer_orders.filter(order_date__gte=from_date)
        if to_date:
            customer_orders = customer_orders.filter(order_date__lte=to_date)
        if warehouse_uuid:
            customer_orders = customer_orders.filter(product__warehouse__uuid=warehouse_uuid)

        total_units_orders = customer_orders.aggregate(Sum('units_ordered'))
        total_ordered_price = customer_orders.aggregate(Sum('total'))

        data = {"total_units_orders": total_units_orders,
                "total_ordered_price": total_ordered_price}

        return Response(json.dumps(data))
