from rest_framework import serializers

from .models import TypeGood


class TypeGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGood
        fields = '__all__'
