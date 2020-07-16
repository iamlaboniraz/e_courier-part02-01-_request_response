from django.contrib.admin import ModelAdmin, register
# from django.contrib import admin
from .models import Profile,contact,CommentBox
# Register your models here.
@register(Profile)
class PersonAdmin(ModelAdmin):
    list_display = ('user', 'factoryName',)
    icon_name = 'face'

@register(contact)
class ContactAdmin(ModelAdmin):
    list_display = ('factoryname', 'Message',)
    icon_name = 'contact_mail'

@register(CommentBox)
class CommentBoxAdmin(ModelAdmin):
    list_display = ('name',)
    icon_name = 'person'