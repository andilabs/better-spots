from django.conf import settings
from django.contrib.gis.geos import fromstr, Point

from rest_framework.serializers import (
    BooleanField,
    CharField,
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ReadOnlyField,
)
from rest_framework.pagination import PaginationSerializer

from core.models import Spot, Rating, UsersSpotsList
from accounts.models import SpotUser


class SpotUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = SpotUser
        fields = ('url', 'mail_verified', 'email')


class RatingSerializer(HyperlinkedModelSerializer):
    spot = HyperlinkedRelatedField(read_only=True, view_name='spot-detail')
    spot_pk = PrimaryKeyRelatedField(queryset=Spot.objects.all())
    is_enabled = BooleanField()

    class Meta:
        model = Rating
        fields = (
            'url',
            'is_enabled',
            'friendly_rate',
            'spot',
            'spot_pk',
            'facilities',
        )


class SpotListSerializer(HyperlinkedModelSerializer):
    www_url = ReadOnlyField()
    id = ReadOnlyField()
    thumbnail_venue_photo = ReadOnlyField()
    location = CharField(required=True)

    class Meta:
        model = Spot
        fields = (
            'pk',
            'url',
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
        )

    def to_internal_value(self, data):
        ret = super(SpotListSerializer, self).to_internal_value(data)

        if isinstance(data['location'], basestring):
            ret['location'] = Point(
                eval(data['location'])['longitude'],
                eval(data['location'])['latitude']
            )

        elif isinstance(data['location'], dict):
            ret['location'] = Point(
                data['location']['longitude'],
                data['location']['latitude']
            )

        else:
            ret['location'] = Point()

        return ret

    def to_representation(self, instance):
        ret = super(SpotListSerializer, self).to_representation(instance)

        if ret.get('location'):
            pnt = fromstr(ret['location'])
            ret['location'] = {
                'longitude': pnt.coords[0],
                'latitude': pnt.coords[1]
            }
        else:
            ret['location'] = None

        ret['www_url'] = instance.www_url

        ret['thumbnail_venue_photo'] = "http://%s%s" % (
            settings.INSTANCE_DOMAIN,
            instance.thumbnail_venue_photo
        ) if instance.thumbnail_venue_photo else None

        return ret


class SpotDetailSerializer(SpotListSerializer):
    ratings = RatingSerializer(read_only=True, many=True)
    friendly_rate = ReadOnlyField()
    is_enabled = ReadOnlyField()

    class Meta:
        model = Spot


class SpotWithDistanceSerializer(SpotListSerializer):

    def to_representation(self, instance):
        ret = super(
            SpotWithDistanceSerializer, self).to_representation(instance)
        ret['distance'] = instance.distance.km
        return ret


class PaginetedSpotWithDistanceSerializer(PaginationSerializer):

    class Meta:
        object_serializer_class = SpotWithDistanceSerializer


class FavouritesSpotsListSerializer(HyperlinkedModelSerializer):
    spot = SpotListSerializer(read_only=True)
    spot_pk = PrimaryKeyRelatedField(
        queryset=Spot.objects.all())

    class Meta:
        model = UsersSpotsList
        fields = ('url', 'spot', 'data_added', 'spot_pk')
