from django import forms
from .models import driver_profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DriverRegisterForm(UserCreationForm):
    email = forms.EmailField()
    car_details = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username', 'email', 'car_details', 'phone', 'password1', 'password2']

class DriverUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email',]


class DriverProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = driver_profile
        fields = ['image','status']
 ##############################

class deliverForm(forms.ModelForm):
	class Meta:
		model = driver_profile
		fields = ['name', 'car_details', 'phone', 'status']
