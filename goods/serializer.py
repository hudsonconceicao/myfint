from rest_framework import serializers

from .models import TypeGoods


class TypeGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGoods
        fields = '__all__'
