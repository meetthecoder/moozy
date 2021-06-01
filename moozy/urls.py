"""moozy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import ValidatePhoneSendOTP, ValidateOTP, Register
from restaurant.views import RestaurantMenuView, RestaurantProfileView, RestaurantProfileUpdate, , RestaurantInfoView
from moozy_admin.views import MenuView, CategoryView, AttributeView

urlpatterns = [
    path('falcon/', admin.site.urls),
    path('validate_phone/', ValidatePhoneSendOTP.as_view()),
    path('validate_otp/', ValidateOTP.as_view()),
    path('register/', Register.as_view()),
    path('resmenu/', RestaurantMenuView.as_view(), name='resmenu'),
    path('resprofile/', RestaurantProfileView.as_view()),
    path('resprofileupdate/<int:pk>/', RestaurantProfileUpdate.as_view()),
    path('category/', CategoryView.as_view(), name='AdminCategory'),
    path('menu/', MenuView.as_view(), name='AdminMenu'),
    path('attribute/', AttributeView.as_view(), name='AdminAttribute'),
    path('resinfo/<int:pk>/', RestaurantInfoView.as_view(), name='Restaurant Info'),

]
