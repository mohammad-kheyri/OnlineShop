from django import forms
from .models import BillingDetails

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['phone_number', 'country', 'city', 'address_line1', 'address_line2', 'postal_code']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'country' : forms.TextInput(attrs={'class': 'form-control'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'address_line1' : forms.TextInput(attrs={'class': 'form-control'}),
            'address_line2' : forms.TextInput(attrs={'class': 'form-control' }),
            'postal_code' : forms.TextInput(attrs={'class': 'form-control'}),
        }