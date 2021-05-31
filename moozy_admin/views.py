from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Menu, FoodCategory, AttributeCategory
from .serializers import MenuSerializer, CategorySerializer, AttributeSerializer


class CategoryView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = CategorySerializer


class MenuView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class AttributeView(ListAPIView):
    queryset = AttributeCategory.objects.all()
    serializer_class = AttributeSerializer
