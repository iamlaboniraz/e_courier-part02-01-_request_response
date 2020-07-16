from django.contrib.admin import ModelAdmin, register
# from django.contrib import admin
from .models import Industry,PriceSet,Location
from .models import IndustryName

# Register your models here.
@register(Industry)
class IndustryAdmin(ModelAdmin):
    list_display = ('industry_name','location','address','Telephone',)
    icon_name = 'account_balance'
@register(PriceSet)
class PriceSetAdmin(ModelAdmin):
    list_display = ('location1','location2','price',)
    icon_name = 'list'

@register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('location',)
    icon_name = 'add_location'

@register(IndustryName)
class IndustryNameAdmin(ModelAdmin):
    list_display = ('name',)
    icon_name = 'add_box'
# class industryAdmin(admin.ModelAdmin):
#     fields = ['industry_name', 'location','address', 'Telephone', 'Fax', 'product']
#     list_display = ['industry_name', 'location','address', 'Telephone', 'Fax', 'product']
#     list_editable = ['industry_name', 'location','address', 'Telephone', 'Fax', 'product']
#     list_display_links = None
#
# class PriceSetAdmin(admin.ModelAdmin):
#     fields = ['location1', 'location2', 'price']
#     list_display = ['location1', 'location2', 'price']
#     list_editable = ['location1', 'location2', 'price']
#     list_display_links = None
# admin.site.register(Industry,industryAdmin)
# admin.site.register(PriceSet,PriceSetAdmin)
# admin.site.register(Location)
# admin.site.register(IndustryName)
