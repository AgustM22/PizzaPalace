from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    NameCardholder = models.CharField(max_length=255)
    CardNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999999999)])
    ExpirationDate = models.DateField()
    CVC = models.PositiveIntegerField(validators=[MaxValueValidator(999)])

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255,)
    ProfilePic = models.CharField(max_length=9999,blank=True,null=True)
    StreetName = models.CharField(max_length=255)
    HouseNumber = models.CharField(max_length=255)
    City  = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    PostalCode = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    CIP = models.ForeignKey(CreditCard, on_delete=models.CASCADE,blank=True,null=True)