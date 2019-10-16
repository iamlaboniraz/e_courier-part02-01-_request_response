from django import forms

## -- from models -- ##
from .models import delivery_product,types_of_product
## ----
## -- for product delivery Form -- ##
class deliverForm(forms.ModelForm):
	OPTIONS = (
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
        )
	OPTIONS2 = (
		('0', '0'),
		('1', '1')
	)
	order_status = forms.ChoiceField(choices=OPTIONS2)
	payment_option = forms.ChoiceField(choices=OPTIONS)
	class Meta:
		model=delivery_product
		fields=['from_location','to_location','product_type','image','phone','order_status','weight','Date','payment_option']
		labels={
		      'from_location':'From Location : ',
		      'to_location':'To Location : ',
		      'product_type' :'Product Type : ',
		      'weight':'Weight : ',
		      'image':'Product Picture :',
		      'Date':'Date :',
		      'payment_option':'payment option',
		      'phone':'phone',
			'order_status':'order_status',
		     }
