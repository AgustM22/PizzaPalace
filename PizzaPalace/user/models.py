from django.db import models

# Create your models here.
class Users(models.Model):
    FullName = models.CharField(max_length=255)
    UserName = models.CharField(max_length=255)
    Password = models.CharField(max_length=20)
    admin = models.BooleanField(default=False)
    profilepic = models.CharField(max_length=9999) #Need to change
    creditcard = models.CharField(max_length=255) #Need to change mabye credit card can be its own table with user id attached
    StreetName = models.CharField(max_length=255)
    HouseNumber = models.CharField(max_length=255)
    City  = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    PostalCode = models.CharField(max_length=255)
    
