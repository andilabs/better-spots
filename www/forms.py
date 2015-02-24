import datetime
from bootstrap3_datetime.widgets import DateTimePicker

from django import forms


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
