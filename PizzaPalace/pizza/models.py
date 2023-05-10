from django.db import models
from user.models import UserProfile

#Moved Users Model to the user folder. ;)

class Tags(models.Model):
    name = models.CharField(max_length=255)

class Foodgroup(models.Model):
    name = models.CharField(max_length=255)

class Topping(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    FID = models.ForeignKey(Foodgroup, on_delete=models.CASCADE, null=True, blank=True)

class HasT(models.Model):
    TID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    TGID = models.ForeignKey(Tags, on_delete=models.CASCADE)    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pricesmall = models.FloatField()
    pricemedium = models.FloatField()
    pricelarge = models.FloatField()
    pic = models.CharField(max_length=9999)

class HasP(models.Model):
    TID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    pic = models.CharField(max_length=9999)


class Includes(models.Model):
    OID = models.ForeignKey(Offer, on_delete=models.CASCADE)
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    time = models.DateTimeField() 
    UID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
class PartOf1(models.Model):
    OID = models.ForeignKey(Offer, on_delete=models.CASCADE)
    ORID = models.ForeignKey(Order, on_delete=models.CASCADE)

class PartOf2(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    TID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    ORID = models.ForeignKey(Order, on_delete=models.CASCADE)