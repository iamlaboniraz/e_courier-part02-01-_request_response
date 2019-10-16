from django.contrib import admin

from delivery_service.models import DelevaryInfo
from .models import types_of_product,delivery_product
# Register your models here.
admin.site.register(types_of_product)
admin.site.register(delivery_product)
admin.site.register(DelevaryInfo)
