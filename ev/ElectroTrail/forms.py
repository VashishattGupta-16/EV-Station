from django import forms
from .models import Evreview,Vehicle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EvReviewForm(forms.ModelForm):
    class Meta:
        model = Evreview
        fields = ['text', 'photo']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle  # Ensure this is the correct model
        fields = ['company_name', 'vehicle_type', 'model_name', 'vehicle_percentage']
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'border border-gray-300  rounded-md px-3 text-black'})

class userRegistrationform(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model= User
        fields=('username','email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(userRegistrationform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'border border-gray-300  rounded-md px-3 text-black'})
