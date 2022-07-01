from django import forms
from .validators import phone_validator
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Customer
        fields = ["name", "last_name", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
