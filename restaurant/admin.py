from django.contrib import admin
from .models import RestaurantMenu, RestaurantProfile, RestaurantInitialInfo

admin.site.site_header = 'Moozy Admin'


@admin.register(RestaurantMenu)
class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'res_owner', 'rescat', 'res_att', 'resmenu', 'price', 'availability']


@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ['restaurant_registration_id', 'name', 'res_user', 'registration_type', 'name_of_proprietor',
                    'manager_name', 'pan_number', 'address', 'gst_no', 'gst_rate', 'fssai_no',
                    'mobile_no', 'email', 'bank_ac_no', 'bank_name', 'ifsc_code', 'km_range',
                    'active_since', 'daily_working_time', 'daily_off', 'evening_timeo', 'evening_timec', 'restaurant_food_type',
                    'restaurant_type', 'special_item', 'registration_date']


@admin.register(RestaurantInitialInfo)
class RestaurantIniInfo(admin.ModelAdmin):
    list_display = ['resuser', 'resname', 'resowner', 'email', 'address', 'area', 'city']
    list_filter = ('area',)
    search_fields = ('resname',)