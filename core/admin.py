from solo.admin import SingletonModelAdmin
from image_cropping import ImageCroppingMixin

from django.conf import settings
from django.contrib import admin


from core.models import (
    Spot,
    Rating,
    Opinion,
    OpinionUsefulnessRating,
    UsersSpotsList,
    Instance
)


hstore_fields = [field['name'] for field in settings.HSTORE_SCHEMA]


# from django.contrib.gis import admin
# from django.contrib.gis import forms
# from django.contrib.gis.db import models

# class YourClassAdminForm(forms.ModelForm):
#     location = forms.PointField(widget=forms.OSMWidget(attrs={
#             'display_raw': True}))


class SpotAdmin(
    ImageCroppingMixin,
    # admin.GeoModelAdmin,
    admin.ModelAdmin):
    # form = YourClassAdminForm

    add_form_template = "admin/spots/add_form.html"
    change_form_template = "admin/spots/change_form.html"

    list_display = (
        'name',
        'friendly_rate',
        'address_city',
        'is_enabled',
        'is_certificated')

    list_filter = ('address_city', 'is_enabled', 'spot_type')

    search_fields = ('name', 'address_city', 'address_street')

    exclude = ('location',)

    fieldsets = (
        (None,
            {'fields': (
                'name',
                'spot_slug',
                'spot_type',
                'is_certificated')}),

        ('Address',
            {'fields': (
                # 'google_maps_admin_widget',
                # 'latitude',
                # 'location',
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

    readonly_fields = tuple([
        # 'google_maps_admin_widget',
        # 'latitude',
        # 'longitude',
        'is_enabled',
        'friendly_rate',
        'spot_slug'] + hstore_fields)


class RatingAdmin(admin.ModelAdmin):
    list_display = [
        'spot', 'friendly_rate', 'is_enabled'] + hstore_fields + ['user']


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
