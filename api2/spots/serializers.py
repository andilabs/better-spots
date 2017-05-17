from rest_framework import serializers

from api2.serializers import GeoPointSerializerField
from core.models.spots import Spot



class SpotSerializer(serializers.ModelSerializer):
    location = GeoPointSerializerField()


    class Meta:
        model = Spot
        fields = [
            'pk',
            'id',
            'www_url',
            'venue_photo',
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
            # 'friendly_rate_stars',
        ]
