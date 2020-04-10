from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('C', 'Debit or Credit Card'),
    ('P', 'PayPal')
    )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(required=False, widget=forms.TextInput())
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
            'id': 'postcode'

        }))
    postcode = forms.CharField(widget=forms.TextInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
