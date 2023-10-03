from django.db import models

from LocationApp.models import Location
from PackageApp.models import PackageType

class Hoteltype(models.Model):
    name=models.CharField(max_length=30,unique=True)
    is_active=models.BooleanField(default=False)
    rate=models.DecimalField(max_digits=20, decimal_places=2)

class Hotel(models.Model):
    name = models.CharField(max_length=30, unique=True) # unique ?
    is_active = models.BooleanField(default=False)
    rate = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    actual_price=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    description = models.TextField(null=True, blank=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT,null=True,blank=True)
    type = models.ForeignKey(PackageType, on_delete=models.PROTECT,null=True,blank=True)
    address= models.TextField(null=True, blank=False)



