# Generated by Django 3.2.3 on 2021-06-01 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantInitialInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resname', models.CharField(max_length=255, verbose_name='Restaurant Name')),
                ('resowner', models.CharField(max_length=100, verbose_name='Owner Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('area', models.CharField(max_length=100, verbose_name='Area')),
                ('city', models.CharField(choices=[('Jaipur', 'Jaipur'), ('Delhi', 'Delhi'), ('Hyderabad', 'Hyderabad'), ('Pune', 'Pune'), ('Bengaluru', 'Bengaluru'), ('Chennai', 'Chennai'), ('Mumbai', 'Mumbai')], max_length=50, verbose_name='City')),
                ('resuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Restaurant Number')),
            ],
        ),
    ]
