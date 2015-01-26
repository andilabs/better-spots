from rest_framework import serializers
from demo.models import (
    Spot, Raiting, Opinion, OpinionUsefulnessRating, SpotUser)#, OtoFoto)

from django.contrib.gis.geos import fromstr

# class OtoFotoSerializer(serializers.HyperlinkedModelSerializer):
#     obrazek_full = serializers.Field()

#     class Meta:
#         model = OtoFoto
#         fields = ('url', 'obrazek', 'obrazek_full')


class SpotUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SpotUser
        fields = ('url', 'mail_verified', 'email')


class OpinionUsefulnessRatingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='opinion-detail')
    user = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='dogspotuser-detail')

    class Meta:
        model = OpinionUsefulnessRating
        fields = ('url', 'opinion', 'vote', 'user')


class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    raiting = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='raiting-detail')
    opinion_usefulnes_raitings = OpinionUsefulnessRatingSerializer(
        read_only=True)

    class Meta:
        model = Opinion
        fields = (
            'opinion_text', 'url', 'raiting', 'opinion_usefulnes_raitings')


class RaitingSerializer(serializers.HyperlinkedModelSerializer):

    opinion = OpinionSerializer(read_only=True)
    spot = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='spot-detail')
    user = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='dogspotuser-detail')
    is_enabled = serializers.BooleanField()

    class Meta:
        model = Raiting
        fields = (
            'url', 'is_enabled', 'friendly_rate', 'spot', 'opinion', 'user')


class SpotListSerializer(serializers.ModelSerializer):

    class Meta:
        # exclude = ('location',)
        model = Spot

    def to_representation(self, instance):
        ret = super(SpotListSerializer, self).to_representation(instance)
        pnt = fromstr(ret['location'])
        ret['location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        # ret['distance'] = instance.distance.km
        ret['longitude'] = pnt.coords[0]
        ret['latitude'] = pnt.coords[1]
        return ret


class SpotDetailSerializer(SpotListSerializer):
    # raitings = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='raiting-detail')
    # raitings = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='pk'
    # )
    raitings = RaitingSerializer(read_only=True, many=True)

    class Meta:
        model = Spot

    # def to_representation(self, instance):
    #     ret = super(SpotDetailSerializer, self).to_representation(instance)
    #     pnt = fromstr(ret['location'])
    #     ret['location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
    #     # ret['distance'] = instance.distance.km
    #     ret['longitude'] = pnt.coords[0]
    #     ret['latitude'] = pnt.coords[1]
    #     return ret


class SpotWithDistanceSerializer(SpotListSerializer):
    # id = serializers.Field()
    distance = serializers.ReadOnlyField()

    class Meta:
        # exclude = ('location',)
        model = Spot

    def to_representation(self, instance):
        ret = super(SpotWithDistanceSerializer, self).to_representation(instance)
        # pnt = fromstr(ret['location'])
        # ret['location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        # ret['longitude'] = pnt.coords[0]
        # ret['latitude'] = pnt.coords[1]
        ret['distance'] = instance.distance.km
        return ret
