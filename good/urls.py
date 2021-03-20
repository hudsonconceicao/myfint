from django.urls import path, include
from rest_framework import routers
from .views import TypeGoodSet

router = routers.DefaultRouter()
router.register(r'typeGood', TypeGoodSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
