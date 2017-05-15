from solo.admin import SingletonModelAdmin
from image_cropping import ImageCroppingMixin

from django import forms
from django.contrib import admin
from django.db import models

from core.models import (
    Spot,
    Rating,
    Opinion,
    OpinionUsefulnessRating,
    Instance
)


# hstore_fields = [field['name'] for field in settings.HSTORE_SCHEMA]


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
        'is_accepted',
        'friendly_rate',
        'address_city',
        'is_enabled',
        'is_certificated',
        # 'number_of_ratings',
        'admin_thumbnail_venue_photo',
        'google_maps_static_image',
        'creator',
        'anonymous_creator_cookie',
        'facilities']
    )

    list_filter = (
        'address_city',
        'is_enabled',
        'spot_type',
        'is_certificated',
        'is_accepted',
    )

    search_fields = (
        'name',
        'address_city',
        'address_street'
    )

    fieldsets = (
        (None,
            {'fields': (
                'name',
                'spot_slug',
                'created_at',
                'updated_at',
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
            {'fields': tuple(['friendly_rate', 'is_enabled'])})
    )

    actions = [
        'make_certificated',
        'revoke_certificated',
        'make_accepted',
        'revoke_accepted',
    ]

    readonly_fields = tuple([
        'google_maps_admin_widget',
        'latitude',
        'longitude',
        'is_enabled',
        'friendly_rate',
        'updated_at',
        'created_at',
        'spot_slug'])

    # def number_of_ratings(self, obj):
    #     return obj.ratings__count
    # number_of_ratings.admin_order_field = 'ratings__count'

    def make_certificated(self, request, queryset):
        for spot in queryset:
            spot.is_certificated = True
            spot.save()

    def revoke_certificated(self, request, queryset):
        for spot in queryset:
            spot.is_certificated = False
            spot.save()

    def make_accepted(self, request, queryset):
        for spot in queryset:
            spot.is_accepted = True
            spot.save()

    def revoke_accepted(self, request, queryset):
        for spot in queryset:
            spot.is_accepted = False
            spot.save()


class RatingAdmin(admin.ModelAdmin):
    list_display = [
            'spot',
            'friendly_rate',
            'is_enabled',
            'user',
        ]


admin.site.register(Spot, SpotAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Opinion)
admin.site.register(Instance, SingletonModelAdmin)
admin.site.register(OpinionUsefulnessRating)
