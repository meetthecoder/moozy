from django.shortcuts import render
from .models import RestaurantMenu, RestaurantProfile, RestaurantInitialInfo
from .serializers import RestaurantMenuSerializer, RestaurantProfileSerializer, RestaurantInfoSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView


class RestaurantMenuView(ListAPIView):
    """Restaurant Menu for List View only"""
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer


class RestaurantProfileView(ListCreateAPIView):
    """Restaurant Profile for Create and Retrieve"""
    queryset = RestaurantProfile.objects.all()
    serializer_class = RestaurantProfileSerializer


class RestaurantProfileUpdate(RetrieveUpdateAPIView):
    """Restaurant Profile Update"""
    queryset = RestaurantProfile.objects.all()
    serializer_class = RestaurantProfileSerializer


class RestaurantInfoView(RetrieveUpdateAPIView):
    """Restaurant Info View"""
    queryset = RestaurantInitialInfo.objects.all()
    serializer_class = RestaurantInfoSerializer
