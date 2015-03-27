from image_cropping import ImageCroppingMixin

from django.conf import settings
from django.contrib import admin


from core.models import (
    Spot, Rating, Opinion, OpinionUsefulnessRating, UsersSpotsList)


hstore_fields = [field['name'] for field in settings.HSTORE_SCHEMA]


class SpotAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_rate',
        'address_city',
        'is_enabled',
        'is_certificated')

    list_filter = ('address_city', 'is_enabled', 'spot_type')

    search_fields = ('name', 'address_city', 'address_street')

    exclude = ('location',)

    readonly_fields = [
        'is_enabled', 'friendly_rate', 'spot_slug'] + hstore_fields

    fieldsets = (
        (None,
            {'fields': (
                'name',
                'spot_slug',
                'spot_type',
                'is_certificated')}),

        ('Address',
            {'fields': (
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
admin.site.register(OpinionUsefulnessRating)
admin.site.register(UsersSpotsList, UsersSpotsListAdmin)
