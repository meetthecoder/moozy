from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import Group
from .models import PhoneOTP
admin.site.register(PhoneOTP)
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'phone', 'active',)
    list_filter = ('staff', 'active')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')
        }),
    )

    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
