from django import forms
from django.core.validators import validate_email
from .validators import phone_validator
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email])
    phone = forms.CharField(validators=[phone_validator])

    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone']
