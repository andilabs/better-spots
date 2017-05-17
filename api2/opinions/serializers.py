from django.conf import settings
from django.contrib.gis.geos import fromstr, Point

from rest_framework.serializers import (
    BooleanField,
    CharField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    ReadOnlyField,
    DecimalField,
)


class SpotListSerializer(ModelSerializer):
    www_url = ReadOnlyField()
    id = ReadOnlyField()
    thumbnail_venue_photo = ReadOnlyField()
    location = CharField(required=True)
    friendly_rate_stars = ReadOnlyField()
    friendly_rate = DecimalField(max_digits=2, decimal_places=1, coerce_to_string=False)

    class Meta:
        model = Spot
        fields = (
            'pk',
            'id',
            'www_url',
            'thumbnail_venue_photo',
            'location',
            'name',
            'address_street',
            'address_number',
            'address_city',
            'address_country',
            'spot_type',
            'is_accepted',
            'phone_number',
            'email',
            'www',
            'facebook',
            'is_enabled',
            'friendly_rate',
            'is_certificated',
            'friendly_rate_stars',
        )