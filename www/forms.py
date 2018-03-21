from image_cropping import ImageCropWidget
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from captcha.fields import CaptchaField

from django import forms

from core.models.spots import Spot


class AddSpotForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Spot
        fields = (
            'location',
            'name',
            'spot_type',
            'phone_number',
            'www',
        )
        widgets = {
            'location': GooglePointFieldWidget,
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
