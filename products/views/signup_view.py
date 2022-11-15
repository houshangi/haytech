from django.contrib.auth.models import Group
from rest_framework.authtoken.admin import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class SignUpSalesmanAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        email = request.data.get('email', False)
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        new_group = Group.objects.get(name='salesman')
        user.groups.add(new_group)
        return Response({"message": "Salesman created successfully"})


class SignUpCustomerAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        email = request.data.get('email', False)
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        new_group = Group.objects.get(name='customer')
        user.groups.add(new_group)
        return Response({"message": "customer created successfully"})
