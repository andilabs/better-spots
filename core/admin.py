from solo.admin import SingletonModelAdmin
from image_cropping import ImageCroppingMixin

from django import forms
from django.conf import settings
from django.contrib import admin
from django.db import models


from core.models import (
    Spot,
    Rating,
    Opinion,
    OpinionUsefulnessRating,
    UsersSpotsList,
    Instance
)


hstore_fields = [field['name'] for field in settings.HSTORE_SCHEMA]


class SpotLocationForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        label='')


class SpotAdmin(ImageCroppingMixin, admin.ModelAdmin):

    def queryset(self, request):
        qs = super(SpotAdmin, self).queryset(request)
        qs = qs.annotate(models.Count('ratings'))
        return qs

    form = SpotLocationForm

    add_form_template = "admin/spots/add_form.html"
    change_form_template = "admin/spots/change_form.html"

    list_display = tuple([
        'name',
        'friendly_rate',
        'address_city',
        'is_enabled',
        'is_certificated',
        'number_of_ratings',
        'facilities'] + hstore_fields
    )

    list_filter = ('address_city', 'is_enabled', 'spot_type')

    search_fields = ('name', 'address_city', 'address_street')

    fieldsets = (
        (None,
            {'fields': (
                'name',
                'spot_slug',
                'spot_type',
                'is_certificated')}),

        ('Address',
            {'fields': (
                'google_maps_admin_widget',
                'latitude',
                'longitude',
                'location',
                'address_street',
                'address_number',
                'address_city',
                'address_country')}),

        ('Contact details',
            {'fields': (
                'phone_number',
                'email',
                'www',
                'facebook')}),

        ('Photo',
            {'fields': (
                'venue_photo',
                'cropping_venue_photo')}),

        ('Evaluations and facilities calculated based on ratings',
            {'fields': tuple(['friendly_rate', 'is_enabled']+hstore_fields)})
    )

    actions = [
        'make_certificated',
        'revoke_certificated',
    ]

    readonly_fields = tuple([
        'google_maps_admin_widget',
        'latitude',
        'longitude',
        'is_enabled',
        'friendly_rate',
        'spot_slug'] + hstore_fields)

    def number_of_ratings(self, obj):
        return obj.ratings__count
    number_of_ratings.admin_order_field = 'ratings__count'

    def make_certificated(self, request, queryset):
        for spot in queryset:
            spot.is_certificated = True
            spot.save()

    def revoke_certificated(self, request, queryset):
        for spot in queryset:
            spot.is_certificated = False
            spot.save()


class RatingAdmin(admin.ModelAdmin):
    list_display = [
            'spot',
            'friendly_rate',
            'is_enabled',
            'user',
        ] + hstore_fields


class UsersSpotsListAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'spot',
        'user'
    )

    list_filter = ('role', 'user', 'spot')


admin.site.register(Spot, SpotAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Opinion)
admin.site.register(Instance, SingletonModelAdmin)
admin.site.register(OpinionUsefulnessRating)
admin.site.register(UsersSpotsList, UsersSpotsListAdmin)
