from django.contrib.admin import ModelAdmin, register
# from django.contrib import admin

from delivery_service.models import DelevaryInfo
from .models import TypesOfProduct, DeliveryProduct,OrderUpdate
# Register your models here.
@register(DelevaryInfo)
class DelevaryInfoAdmin(ModelAdmin):
    list_display = ('order', 'driver','industry','rating',)

    icon_name = 'directions_bike'


@register(TypesOfProduct)
class typesofproductAdmin(ModelAdmin):
    list_display = ('title',)
    icon_name = 'add'

@register(DeliveryProduct)
class DeliveryProductAdmin(ModelAdmin):
    list_display = ('from_location', 'to_location',)
    icon_name = 'child_friendly'


@register(OrderUpdate)
class OrderAdmin(ModelAdmin):
    list_display = ('update_id', 'order_id',)
    icon_name ='edit_location'


