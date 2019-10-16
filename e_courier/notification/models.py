from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from delivery_service.models import delivery_product
# # Create your models here.

# class Notification(models.Model):
#     title = models.CharField(max_length=256)
#     message = models.TextField()
#     viewed = models.BooleanField(default=False)
#     user = models.ForeignKey(User,on_delete=False)
#     delivery=models.ForeignKey(delivery_product,on_delete=False)

# @receiver(post_save,sender=delivery_product)
# def create_welcome_message(sender,**kwargs):
#     if kwargs.get('create',False):
#         Notification.objects.create(delivery=kwargs.get('instance'),
#         title = "Wait a few minutes please!",
#         message = "We are searching driver!")
