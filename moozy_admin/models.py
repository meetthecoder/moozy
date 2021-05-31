from django.db import models
from user.models import RestaurantUser


class FoodCategory(models.Model):
    """Admin Food Category"""
    name = models.CharField(max_length=50, verbose_name='Name')
    image = models.ImageField(upload_to="media/food_category/", verbose_name='Image')

    def __str__(self):
        return self.name


class Menu(models.Model):
    """Admin Menu"""
    name = models.CharField(max_length=50, verbose_name='Name')
    image = models.ImageField(upload_to="media/menu_images/", verbose_name='Image')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='cat', verbose_name='Category')
    food_choices = (
        ('Veg', 'Veg'),
        ('Nonveg', 'Nonveg'),
        ('Both', 'Both'),
    )
    food_type = models.CharField(max_length=50, blank=False, null=True, choices=food_choices, verbose_name='Food Type')

    def __str__(self):
        return self.name


class AttributeCategory(models.Model):
    """Attribute Category"""
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to="media/attr_images/", verbose_name='Image')

    def __str__(self):
        return self.name


