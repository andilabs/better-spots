import datetime

from image_cropping import ImageCropWidget

from django import forms

from core.models.spots import Spot


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    mail = forms.EmailField()
    date = forms.DateField(initial=datetime.date.today)
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

            'venue_photo',
            'cropping_venue_photo',

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
            'venue_photo': ImageCropWidget,

        }


class EditSpotPhotoForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = (
            'venue_photo',
            'cropping_venue_photo',
        )
        widgets = {
            'venue_photo': ImageCropWidget,
        }
