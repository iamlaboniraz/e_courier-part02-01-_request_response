from django.contrib import admin
from .models import driver_profile
# Register your models here.
class driverProfileAdmin(admin.ModelAdmin):
    fields = ['name', 'car_details', 'phone', 'status']
    search_fields = ['status', 'car_details']
    list_filter = ['status', 'car_details', 'name' ,'phone']
    list_display = ['status', 'car_details', 'name', 'phone']
    list_editable = ['status']
    list_display_links = None
admin.site.register(driver_profile,driverProfileAdmin)
