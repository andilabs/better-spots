import datetime
from bootstrap3_datetime.widgets import DateTimePicker

from django import forms

from core.models import Spot


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,)
    mail = forms.EmailField()

    date = forms.DateField(
        initial=datetime.date.today,
        widget=DateTimePicker(
            options={
                "format": "DD-MM-YYYY",
                "pickTime": False,
                "showToday": True,
                })
        )

    message = forms.CharField(widget=forms.Textarea)


class AddSpotForm(forms.ModelForm):

    class Meta:
        model = Spot
        fields = (
            'name',
            'spot_type',
            'phone_number',
            'www',
            'facebook',

            'location',
            'address_street',
            'address_number',
            'address_city',
            'address_country',
        )
        widgets = {
            'location': forms.HiddenInput(
                attrs={
                    'id': 'location',
                }),
            'address_street': forms.TextInput(
                attrs={
                    'style': 'background-color: #eee',
                    'id': 'address_street',
                }),
            'address_number': forms.TextInput(
                attrs={
                    'style': 'background-color: #eee',
                    'id': 'address_number',
                }),
            'address_city': forms.TextInput(
                attrs={
                    'style': 'background-color: #eee',
                    'id': 'address_city',
                }),
            'address_country': forms.TextInput(
                attrs={
                    'style': 'background-color: #eee',
                    'id': 'address_country',
                }),
        }
