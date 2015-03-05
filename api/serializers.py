from django.conf import settings
from django.contrib.gis.geos import fromstr, Point
from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from core.models import (
    Spot, Raiting, Opinion, OpinionUsefulnessRating, SpotUser)


class SpotUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SpotUser
        fields = ('url', 'mail_verified', 'email')


class OpinionUsefulnessRatingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='opinion-detail')
    user = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='spotuser-detail')

    class Meta:
        model = OpinionUsefulnessRating
        fields = ('url', 'opinion', 'vote', 'user')


class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    raiting = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='raiting-detail')
    opinion_usefulnes_raitings = OpinionUsefulnessRatingSerializer(
        read_only=True, many=True)

    class Meta:
        model = Opinion
        fields = (
            'opinion_text', 'url', 'raiting', 'opinion_usefulnes_raitings')


class RaitingSerializer(serializers.HyperlinkedModelSerializer):

    opinion = OpinionSerializer(read_only=True)
    spot = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='spot-detail')
    user = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='spotuser-detail')
    is_enabled = serializers.BooleanField()

    class Meta:
        model = Raiting
        fields = (
            'url', 'is_enabled', 'friendly_rate', 'spot', 'user', 'opinion')


class SpotListSerializer(serializers.HyperlinkedModelSerializer):
    www_url = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    thumbnail_venue_photo = serializers.ReadOnlyField()
    location = serializers.CharField(required=True)

    class Meta:
        model = Spot
        exclude = tuple(['spot_slug', 'cropping_venue_photo', 'venue_photo'] + [field['name'] for field in settings.HSTORE_SCHEMA])

    def to_internal_value(self, data):
        ret = super(SpotListSerializer, self).to_internal_value(data)
        if isinstance(data['location'], basestring):
           ret['location'] = Point(eval(data['location'])['longitude'], eval(data['location'])['latitude'])
        elif isinstance(data['location'], dict):
            ret['location'] = Point(data['location']['longitude'], data['location']['latitude'])
        else:
            ret['location'] = Point()
        return ret

    def to_representation(self, instance):
        ret = super(SpotListSerializer, self).to_representation(instance)

        if ret.get('location'):
            pnt = fromstr(ret['location'])
            ret['location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        else:
            ret['location'] = None

        ret['facilities'] = dict([
            (i[0], eval('None' if not i[1] else i[1])) for i in ret['facilities'].iteritems()
        ])
        ret['www_url'] = instance.www_url
        ret['thumbnail_venue_photo'] = instance.thumbnail_venue_photo
        return ret


class SpotDetailSerializer(SpotListSerializer):
    raitings = RaitingSerializer(read_only=True, many=True)

    class Meta:
        model = Spot
        exclude = tuple(['spot_slug']+[field['name'] for field in settings.HSTORE_SCHEMA])


class SpotWithDistanceSerializer(SpotListSerializer):
    distance = serializers.ReadOnlyField()

    def to_representation(self, instance):
        ret = super(SpotWithDistanceSerializer, self).to_representation(instance)
        ret['distance'] = instance.distance.km
        return ret


class PaginetedSpotWithDistanceSerializer(PaginationSerializer):
        class Meta:
            object_serializer_class = SpotWithDistanceSerializer
