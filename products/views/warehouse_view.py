from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import WareHouse
from ..permissions import SalesManAccessPermission
from ..seriailzers import WareHouseSerializer


class WareHouseAPIView(ListCreateAPIView):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    permission_classes = [SalesManAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class WareHouseDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    permission_classes = [SalesManAccessPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]


