from django.db import models
import datetime

from django.forms import DecimalField
from django.utils import timezone
from measurement.measures import Weight
from django_measurement.models import MeasurementField

# Create your models here.
from account.models import Profile
from driver.models import DriverProfile
from industry.models import Industry, PriceSet, Location, IndustryName

OPTIONS2 = (
    ('0', '0'),
    ('1', '1')
)
OPTIONS3 = (
    ('Narayanganj', 'Narayanganj'),
    ('Gazipur', 'Gazipur'),
    ('Bonani', 'Bonani')
)
class TypesOfProduct(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class DeliveryProduct(models.Model):
    # order_id = models.AutoField(primary_key=True)
    from_location = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='from_location')
    to_location = models.ForeignKey(Industry, on_delete=models.CASCADE,related_name='to_location')
    PresentAddress = models.CharField(max_length=255,choices=OPTIONS3)
    product_type = models.ForeignKey(TypesOfProduct,on_delete=models.CASCADE)
    weight = MeasurementField(measurement=Weight,null=True,blank=True)
    Date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    phone = models.CharField(max_length=20)
    Bill = models.IntegerField(null=True,blank=True)
    order_status = models.CharField(max_length=100, choices=OPTIONS2, default="0")
    def __str__(self):
        return f"From Location :{self.from_location} and To location : {self.to_location} and Phone Number :{self.phone} and Product Type :{self.product_type}"


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    # timestamp = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True,blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True,blank=True)
    # latitude = models.IntegerField(null=True,blank=True)
    # longitude = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.update_desc[0:7]+"....."


class DelevaryInfo(models.Model):
    RATING_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='FactoryInvoice')
    order = models.ForeignKey(DeliveryProduct, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, null=True, blank=True)
    industry = models.ForeignKey(PriceSet, on_delete=models.CASCADE, null=True, blank=True,related_name='Bill')
    rating = models.CharField(max_length=100, choices=RATING_RANGE, default="3")
    def __str__(self):
        return f"{self.client} {self.order} {self.driver} {self.industry}"

    def __int__(self):
        return self.industry

    def sum_total(self):
        return self.industry

