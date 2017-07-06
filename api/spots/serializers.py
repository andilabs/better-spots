from rest_framework import serializers

from accounts.models import User
from api.serializers import GeoPointSerializerField
from core.models.spots import Spot
from utils.models import Tag


class SpotSerializer(serializers.ModelSerializer):
    location = GeoPointSerializerField()
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='text'
    )
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.none())

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
            'tags',
            'creator',
        ]

    def __init__(self, *args, **kwargs):
        super(SpotSerializer, self).__init__(*args, **kwargs)
        if 'request' in self.context and self.context['request'] and hasattr(self.context['request'].user, 'pk'):
            self.fields['creator'].queryset = User.objects.filter(pk=self.context['request'].user.pk)
