
import datetime

from django import forms
#from django.contrib.auth import authenticate

# from django.core.mail import EmailMessage
from bootstrap3_datetime.widgets import DateTimePicker

from demo.models import SpotUser
#from datetimewidget.widgets import DateTimeWidget


# dateTimeOptions = {
#     'id': "date",
#     'format': 'dd-mm-yyyy',
#     'autoclose': 'true',
#     'showMeridian': 'true',
#     'weekStart': 1,
#     'startView': 2,
#     'minView': 2,
#     'maxView': 2,
#     'todayBtn': 'true'
# }


class UserCreationForm(forms.ModelForm):

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput)

    class Meta:
        model = SpotUser
        fields = ('email', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=False):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,)
    mail = forms.EmailField()
    # date = forms.DateTimeField(
    #     widget=DateTimeWidget(options=dateTimeOptions),
    # )

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

