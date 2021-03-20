from rest_framework import viewsets

from .models import TypeGoods
from .serializer import TypeGoodsSerializer


# Create your views here.


class TypeGoodsSet(viewsets.ModelViewSet):
    """ The viewSet TypeGood model"""
    queryset = TypeGoods.objects.all()
    serializer_class = TypeGoodsSerializer
