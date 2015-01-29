from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from core.models import SpotUser, Spot, Raiting, Opinion, OpinionUsefulnessRating#, Rental
from django import forms
import random
import string
from rest_framework import serializers
from django.core.mail import EmailMessage


import urllib
import json
from django.utils.http import urlquote
YOUR_API_KEY = "AIzaSyBj2VxTkcBPQ9yOXerWQUil-pzMuTaz4Ao"


def geocode(addr):
    """
        This method for given in parameter address makes request to Google Maps API, and returns latitude and longitude
    """

    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" \
          % (urlquote(addr.replace(' ', '+')))

    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")
    #print info
    #print "%2.5f,%2.5f" % (info['lat'],info['lng'])
    return info


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
        fields = ('email', 'mail_verified',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


def get_new_password():
    new_random_password = ''.join(
        random.choice(string.ascii_uppercase + string.digits
                      ) for _ in range(settings.DESIRED_PASSWORD_LENGTH))
    return new_random_password


class UserChangeForm(forms.ModelForm):

    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = SpotUser
        fields = ('email', 'password', 'mail_verified', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        cleaned_data = self.cleaned_data
        old_status = SpotUser.objects.get(email=cleaned_data['email'])
        if ((old_status.mail_verified is False or old_status.mail_verified is None) and
                cleaned_data['mail_verified'] is True):
            new_pass = get_new_password()
            user.set_password(new_pass)
            send_credentials(user.email, new_pass)
        if commit:
            user.save()
        return user


class SpotUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'mail_verified', 'is_admin')
    list_filter = ('is_admin', 'mail_verified')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mail_verified')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mail_verified', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class DogAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SpotAdmin(admin.ModelAdmin):
    exclude = ('location',)


admin.site.register(SpotUser, SpotUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Raiting)
admin.site.register(Opinion)
admin.site.register(OpinionUsefulnessRating)
