from rest_framework import serializers
from .models import Menu, FoodCategory, AttributeCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeCategory
        fields = '__all__'
