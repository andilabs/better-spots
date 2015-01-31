from django.contrib.gis.geos import fromstr
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

    class Meta:
        model = Spot
        exclude = ('spot_slug', )

    def to_representation(self, instance):
        ret = super(SpotListSerializer, self).to_representation(instance)
        pnt = fromstr(ret['location'])
        ret['location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        ret['www_url'] = instance.www_url
        return ret


class SpotDetailSerializer(SpotListSerializer):
    raitings = RaitingSerializer(read_only=True, many=True)

    class Meta:
        model = Spot


class SpotWithDistanceSerializer(SpotListSerializer):
    distance = serializers.ReadOnlyField()

    def to_representation(self, instance):
        ret = super(SpotWithDistanceSerializer, self).to_representation(instance)
        ret['distance'] = instance.distance.km
        return ret


class PaginetedSpotWithDistanceSerializer(PaginationSerializer):
        class Meta:
            object_serializer_class = SpotWithDistanceSerializer
