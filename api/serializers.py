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

from accounts.models import User
from accounts.models import UserFavouritesSpotList
from core.models.ratings import Rating
from core.models.spots import Spot


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('mail_verified', 'email')


class RatingSerializer(ModelSerializer):

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


class SpotListSerializer(ModelSerializer):

    class Meta:
        model = Spot
        fields = (
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

        ret['thumbnail_venue_photo'] = "http://%s%s" % (
            settings.INSTANCE_DOMAIN,
            instance.thumbnail_venue_photo
        ) if instance.thumbnail_venue_photo else None

        if not instance.email:
            ret['email'] = ""

        ret['facilities'] = {}#{settings.FACILITIES_CODE_VERBOSE_MAP[k]: bool(eval(str(v))) for k, v in instance.facilities.items()}
        ret['friendly_rate_stars'] = '*'*int(round(instance.friendly_rate))
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


class FavouritesSpotsListSerializer(ModelSerializer):
    spot = SpotListSerializer(read_only=True)

    class Meta:
        model = UserFavouritesSpotList
        fields = (
            'spot',
            'created_at',
        )
