from django import forms

## -- from models -- ##
from industry.models import Industry
from .models import DeliveryProduct, TypesOfProduct, DelevaryInfo, OrderUpdate


## ----
## -- for product delivery Form -- ##
class deliverForm(forms.ModelForm):
    class Meta:
        model = DeliveryProduct
        fields = ['from_location', 'to_location', 'PresentAddress','product_type', 'phone', 'weight']
        labels = {
            'from_location': 'From industry : ',
            'to_location': 'To industry : ',
            'PresentAddress': 'Present Address',
            'product_type': 'Product Type : ',
            'weight': 'Weight : ',
            'image': 'Product Picture :',
            'phone': 'phone',
        }


class deliverFormEdit(forms.ModelForm):
    class Meta:
        model = DeliveryProduct
        fields = ['from_location', 'to_location','Date','order_status', 'product_type', 'phone', 'weight']
        labels = {
            'from_location': 'From Location : ',
            'to_location': 'To Location : ',
            'product_type': 'Product Type : ',
            'weight': 'Weight : ',
            'image': 'Product Picture :',
            'Date': 'Date',
            'order_status': 'order status',
            'phone': 'phone',
        }


class DelevaryInfoForm(forms.ModelForm):
    class Meta:
        model = DelevaryInfo
        fields = ['rating']




class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = OrderUpdate
        fields = ['update_id', 'order_id', 'update_desc', 'timestamp']
        labels = {
            'update_id': 'Update ID : ',
            'order_id': 'Order ID : ',
            'update_desc': 'Update Description',
            'timestamp': 'Time : ',
        }

class OrderUpdateLocationForm(forms.ModelForm):
    class Meta:
        model = OrderUpdate
        fields = ['update_id', 'order_id', 'update_desc', 'timestamp']
        labels = {
            'update_id': 'Update ID : ',
            'order_id': 'Order ID : ',
            'update_desc': 'Update Description',
            'timestamp': 'Time : ',
        }


