from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..exceptions import OutOfStockException
from ..seriailzers import OrderSerializer, OrderDetailSerializer
from ..models import Order
from ..permissions import CustomerAccessPermission
from ..models import Product
from rest_framework.permissions import AllowAny, IsAdminUser


class OrderProductAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomerAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        pk = self.request.data['product']
        product = get_object_or_404(Product, pk=pk)
        if product.quantity < self.request.data['units_ordered']:
            raise OutOfStockException("there is not enough Stock in the Warehouse")
        # just assume there is only product per order
        self.request.data['total'] = self.request.data['units_ordered'] * product.price
        self.request.data['owner'] = self.request.user.id

        order_serializer = OrderSerializer(data=self.request.data)
        order_serializer.is_valid()
        order_serializer.save()


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]