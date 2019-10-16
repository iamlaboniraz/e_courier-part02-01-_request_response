from django.db import models
import datetime
from django.utils import timezone
from measurement.measures import Weight
from django_measurement.models import MeasurementField

# Create your models here.
from account.models import Profile
from driver.models import driver_profile

OPTIONS2 = (
		('0', '0'),
		('1', '1')
	)
class types_of_product(models.Model):
	title=models.CharField(max_length=100)
	def __str__(self):
		return self.title

class delivery_product(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    product_type = models.ForeignKey(types_of_product,on_delete=models.CASCADE)
    weight = MeasurementField(measurement=Weight,null=True,blank=True)
    Date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    phone = models.CharField(max_length=20)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=100, choices=OPTIONS2, default="0")
    def __str__(self):
        return f"From Location :{self.from_location} and To location : {self.to_location} and Phone Number :{self.phone} and Product Type :{self.product_type}"

class DelevaryInfo(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(delivery_product, on_delete=models.CASCADE)
    driver = models.ForeignKey(driver_profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.client} {self.order} {self.driver}"
