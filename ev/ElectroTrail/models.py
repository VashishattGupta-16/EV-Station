
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz


# Create your models here.
class Evreview (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240,)
    photo = models.ImageField(upload_to='photo/',blank= True ,null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Details'


# models.py

# models.py

from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
    ]
    PERCENTAGES=[
        ('10', '10%'),
        ('20', '20%'),
        ('30', '30%'),
        ('40', '40%'),
        ('50', '50%'),
        ('60', '60%'),
        ('70', '70%'),
        ('80', '80%'),
        ('90', '90%'),
        ('100', '100%'),
    ]

    company_name = models.CharField(max_length=100)  # Company name
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)  # Vehicle type
    vehicle_percentage = models.CharField(max_length=20, choices=PERCENTAGES, default='0')  # Vehicle type
    model_name = models.CharField(max_length=100)  # Model name of the vehicle
    created_at = models.DateTimeField(auto_now_add=True) #
    upload_to = models.DateTimeField(auto_now=True)
    def get_created_at_ist(self):
        """Return the created_at time in Indian Standard Time (IST)."""
        # Convert created_at to IST
        return self.created_at.astimezone(pytz.timezone('Asia/Kolkata'))

    def __str__(self):
        return f"{self.model_name} - {self.company_name} ({self.vehicle_type})"

