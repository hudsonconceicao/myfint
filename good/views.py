from rest_framework import viewsets

from .models import TypeGood
from .serializer import TypeGoodSerializer


# Create your views here.


class TypeGoodSet(viewsets.ModelViewSet):
    """ The viewSet TypeGood model"""
    queryset = TypeGood.objects.all()
    serializer_class = TypeGoodSerializer
