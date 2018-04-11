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
    distance = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

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
            'distance',
            'category',
        ]

    def get_distance(self, obj):
        # if queryset was filtered by location it will be annotated with distance
        if hasattr(obj, 'distance'):
            return round(obj.distance.km, 1)
        else:
            return None

    def get_category(self, obj):
        return obj.get_spot_type_display()

    def __init__(self, *args, **kwargs):
        super(SpotSerializer, self).__init__(*args, **kwargs)
        if 'request' in self.context and self.context['request'] and hasattr(self.context['request'].user, 'pk'):
            self.fields['creator'].queryset = User.objects.filter(pk=self.context['request'].user.pk)
