from django.db import models
from moozy_admin.models import Menu, FoodCategory, AttributeCategory
from user.models import RestaurantUser


class RestaurantProfile(models.Model):
    """Restaurant Profile Model"""
    restaurant_registration_id = models.CharField(max_length=20, blank=False, unique=True)
    name = models.CharField(max_length=500, verbose_name='Restaurant Name')
    res_user = models.OneToOneField(RestaurantUser, on_delete=models.CASCADE, verbose_name='Restaurant', related_name='restaurantuser')
    registration_type = models.CharField(max_length=100, verbose_name='Registration Type')
    name_of_proprietor = models.CharField(max_length=100, verbose_name='Proprietor Name')
    manager_name = models.CharField(max_length=100, verbose_name='Manager Name')
    pan_number = models.CharField(max_length=20, verbose_name='Pan Card')
    address = models.CharField(max_length=1000, verbose_name='address')
    gst_no = models.CharField(max_length=30, verbose_name='GST No.')
    gst_rate = models.IntegerField(verbose_name='GST Rate(%)')
    fssai_no = models.CharField(max_length=14, verbose_name='FSSAI No.')
    mobile_no = models.CharField(max_length=12, verbose_name='Mobile No.')
    email = models.EmailField(max_length=50, verbose_name='Email')
    bank_ac_no = models.CharField(max_length=25, verbose_name='Bank Account No.')
    bank_name = models.CharField(max_length=50, verbose_name='Bank Name')
    ifsc_code = models.CharField(max_length=50, verbose_name='IFSC Code')
    km_range = models.IntegerField(verbose_name='Range in Km')
    active_since = models.DateField(verbose_name='Active Since')
    daily_working_time = models.TimeField(verbose_name='Restaurant Open(Morning)')
    daily_off = models.TimeField(verbose_name='Restaurant Close(Morning')
    evening_timeo = models.TimeField(verbose_name='Restaurant Open(Evening')
    evening_timec = models.TimeField(verbose_name='Restaurant Close(Evening)')
    restaurant_food_type = (
        ('Veg', 'Veg'),
        ('Nonveg', 'Nonveg'),
        ('Both', 'Both'),
    )
    restaurant_type = models.CharField(max_length=20, choices=restaurant_food_type, verbose_name='Restaurant Type')
    special_item = models.CharField(max_length=100, verbose_name='Special Type')
    registration_date = models.DateTimeField()


class RestaurantMenu(models.Model):
    """Restaurant Menu Model"""
    res_owner = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE, related_name='restarantuser', verbose_name='Restaurant')
    rescat = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, verbose_name='Select Category', related_name='catag')
    res_att = models.ForeignKey(AttributeCategory, on_delete=models.CASCADE,
                                verbose_name='Select Attribute',
                                related_name='attcat')
    resmenu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Select Item', related_name='men')
    price = models.FloatField()
    availability = models.BooleanField(default=True)


class RestaurantInitialInfo(models.Model):
    """Initial Information about Restaurant"""
    resuser = models.OneToOneField(RestaurantUser, on_delete=models.CASCADE,blank=False, verbose_name='Restaurant Number')
    city_choices = (
        ('Jaipur', 'Jaipur'),
        ('Delhi', 'Delhi'),
        ('Hyderabad', 'Hyderabad'),
        ('Pune', 'Pune'),
        ('Bengaluru', 'Bengaluru'),
        ('Chennai', 'Chennai'),
        ('Mumbai', 'Mumbai'),
    )
    resname = models.CharField(max_length=255, blank=False, verbose_name='Restaurant Name')
    resowner = models.CharField(max_length=100, blank=False, verbose_name='Owner Name')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    address = models.TextField(verbose_name='Address')
    area = models.CharField(max_length=100, blank=False, verbose_name="Area")
    city = models.CharField(max_length=50, blank=False, verbose_name='City', choices=city_choices)

