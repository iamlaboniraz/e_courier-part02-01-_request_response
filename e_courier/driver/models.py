from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
# Create your models here.
STATUS_CHOICES = (
    ("Active", "Active"),
    ("Not Available", "Not Available"),
    ("Onrequest","Onrequest"),
)
STATUS_CHOICES2 = (
    ("0", "0"),
    ("1", "1"),
)
class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='DriverProfile')
    name = models.CharField(max_length=100)
    car_details = models.TextField(null=False,blank=False)
    # email = models.EmailField(max_length=70,unique=True)
    phone = models.CharField(max_length=12,null=False,blank=False,unique=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES, default="Active")
    status2 = models.CharField(max_length=100,choices=STATUS_CHOICES2, default="0")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} driver Profile {self.car_details}'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

