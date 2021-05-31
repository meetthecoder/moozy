from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False):
        if not phone:
            raise ValueError('User must have a phone number')

        user_obj = self.model(phone=phone)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone):
        user = self.create_user(phone, password=None, is_staff=True, )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(phone, password=password, is_staff=True, is_admin=True, is_active=True)
        return user


class RestaurantUser(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}', message="Phone number must be entered in the Phone Field")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class PhoneOTP(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}', message="Phone number must be entered in the Phone Field")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    otp = models.CharField(max_length=4, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Number of OTP sent')
    validated = models.BooleanField(default=False, help_text='If it is true, that have validate otp correctly in '
                                                             'second API')

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)



