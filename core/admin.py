from solo.admin import SingletonModelAdmin
from image_cropping import ImageCroppingMixin

from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from core.models.instance import Instance
from core.models.opinions import Opinion, OpinionUsefulnessRating
from core.models.ratings import Rating
from core.models.spots import Spot


class SpotAdmin(ImageCroppingMixin, admin.ModelAdmin):

    def queryset(self, request):
        qs = super(SpotAdmin, self).queryset(request)
        qs = qs.annotate(models.Count('ratings'))
        return qs

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

    list_display = (
        'pk',
        'name',
        'is_accepted',
        'friendly_rate',
        'address_city',
        'is_enabled',
        'is_certificated',
        'admin_thumbnail_venue_photo',
        'google_maps_static_image',
        'creator',
        'anonymous_creator_cookie',
    )

    list_filter = (
        'address_city',
        'is_enabled',
        'spot_type',
        'is_certificated',
        'is_accepted',
        'tags',
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
            {'fields': tuple(['friendly_rate', 'is_enabled', 'tags'])})
    )

    actions = [
        'make_certificated',
        'revoke_certificated',
        'make_accepted',
        'revoke_accepted',
    ]

    readonly_fields = tuple([
        'latitude',
        'longitude',
        'address_street',
        'address_number',
        'address_city',
        'address_country',
        'is_enabled',
        'friendly_rate',
        'updated_at',
        'created_at',
        'spot_slug',
        'tags'])

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
        'pk',
        'spot',
        'friendly_rate',
        'is_enabled',
        'user',
    ]


class OpinionAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'rating',
        'opinion_text',
    ]


admin.site.register(Spot, SpotAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Opinion, OpinionAdmin)
admin.site.register(Instance, SingletonModelAdmin)
admin.site.register(OpinionUsefulnessRating)
