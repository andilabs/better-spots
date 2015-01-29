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

from accounts.forms import UserCreationForm, UserChangeForm


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


class SpotAdmin(admin.ModelAdmin):
    exclude = ('location',)


admin.site.register(SpotUser, SpotUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Raiting)
admin.site.register(Opinion)
admin.site.register(OpinionUsefulnessRating)
