# Generated by Django 3.2.3 on 2021-05-31 01:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the Phone Field', regex='^\\+?1?\\d{9,12}')])),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the Phone Field', regex='^\\+?1?\\d{9,12}')])),
                ('otp', models.CharField(blank=True, max_length=4, null=True)),
                ('count', models.IntegerField(default=0, help_text='Number of OTP sent')),
                ('validated', models.BooleanField(default=False, help_text='If it is true, that have validate otp correctly in second API')),
            ],
        ),
    ]
