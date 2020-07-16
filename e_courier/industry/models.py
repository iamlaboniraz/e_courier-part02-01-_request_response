from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.location}"
class PriceSet(models.Model):
    location1 = models.CharField(max_length=255)
    location2 = models.CharField(max_length=255)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.location1} and {self.location2} and {self.price}"

class IndustryName(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Industry(models.Model):
    industry_name = models.ForeignKey(IndustryName, on_delete=models.CASCADE,related_name='locationSet')
    location = models.ForeignKey(Location, on_delete=models.CASCADE,related_name='locationSet')
    email = models.EmailField(max_length=70,unique=True)
    address = models.CharField(max_length=255)
    Telephone = models.CharField(max_length=255,null=True, blank=True)
    Fax = models.CharField(max_length=255, null=True, blank= True)
    product = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.industry_name}"
