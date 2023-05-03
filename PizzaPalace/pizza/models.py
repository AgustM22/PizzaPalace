from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    admin = models.BooleanField()
    profilepic = models.CharField(max_length=9999)
    creditcard = models.CharField(max_length=255)

class Tags(models.Model):
    name = models.CharField(max_length=255)

class Topping(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

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
    UID = models.ForeignKey(Users, on_delete=models.CASCADE)
    
class PartOf1(models.Model):
    OID = models.ForeignKey(Offer, on_delete=models.CASCADE)
    ORID = models.ForeignKey(Order, on_delete=models.CASCADE)

class PartOf2(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    TID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    ORID = models.ForeignKey(Order, on_delete=models.CASCADE)