from rest_framework import serializers
from .models import RestaurantProfile, RestaurantMenu


class RestaurantMenuSerializer(serializers.ModelSerializer):
    """Restaurant menu serializer"""
    class Meta:
        model = RestaurantMenu
        fields = ['id', 'rescat', 'resmenu', 'price', 'availability']


class RestaurantProfileSerializer(serializers.ModelSerializer):
    """Restaurant Profile Serializer"""
    class Meta:
        model = RestaurantProfile
        fields = ['restaurant_registration_id', 'name', 'res_user', 'registration_type', 'name_of_proprietor',
                    'manager_name', 'pan_number', 'address', 'gst_no', 'gst_rate', 'fssai_no',
                    'mobile_no', 'email', 'bank_ac_no', 'bank_name', 'ifsc_code', 'km_range',
                    'active_since', 'daily_working_time', 'daily_off', 'evening_timeo', 'evening_timec', 'restaurant_food_type',
                    'restaurant_type', 'special_item', 'registration_date']
