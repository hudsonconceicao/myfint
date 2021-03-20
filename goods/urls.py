from django.urls import path, include
from rest_framework import routers
from .views import TypeGoodsSet

router = routers.DefaultRouter()
router.register(r'typeGood', TypeGoodsSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
