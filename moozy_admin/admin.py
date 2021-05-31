from django.contrib import admin

from .models import Menu, FoodCategory, AttributeCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'category', 'food_type']
    search_fields = ['name', 'food_type']


@admin.register(AttributeCategory)
class AttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

