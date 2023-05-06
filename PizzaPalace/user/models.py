from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255)
    profilepic = models.CharField(max_length=9999)
    StreetName = models.CharField(max_length=255)
    HouseNumber = models.CharField(max_length=255)
    City  = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    PostalCode = models.CharField(max_length=255)
    