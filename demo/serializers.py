from rest_framework import serializers
from demo.models import Spot, Raiting, Opinion, OpinionUsefulnessRating


class OpinionUsefulnessRatingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='opinion-detail')

    class Meta:
        model = OpinionUsefulnessRating
        fields = ('url', 'opinion', 'vote')


class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    raiting = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='raiting-detail')
    opinion_usefulnes_raitings = OpinionUsefulnessRatingSerializer(
        read_only=True)

    class Meta:
        model = Opinion
        fields = (
            'opinion_text', 'url', 'raiting', 'opinion_usefulnes_raitings')


class RaitingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = OpinionSerializer(many=False, read_only=True)
    spot = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='spot-detail')

    class Meta:
        model = Raiting
        fields = ('url', 'dogs_allowed', 'friendly_rate', 'spot', 'opinion')


class SpotListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Spot
        fields = ('id', 'url', 'name', 'latitude', 'longitude')


class SpotDetailSerializer(serializers.HyperlinkedModelSerializer):
    friendly_rate = serializers.Field()
    dogs_allowed = serializers.Field()
    raitings = RaitingSerializer(read_only=True)

    class Meta:
        model = Spot
        fields = (
            'id', 'url', 'name', 'latitude', 'longitude', 'address_street',
            'address_number', 'address_city', 'address_country', 'spot_type',
            'is_accepted', 'friendly_rate', 'dogs_allowed', 'phone_number',
            'raitings')


class SpotWithDistanceSerializer(serializers.HyperlinkedModelSerializer):
    distance = serializers.Field()
    friendly_rate = serializers.Field()
    dogs_allowed = serializers.Field()

    class Meta:
        model = Spot
        fields = (
            'id', 'distance', 'url', 'name', 'latitude', 'longitude',
            'address_street', 'address_number', 'address_city',
            'address_country', 'spot_type', 'is_accepted', 'friendly_rate',
            'dogs_allowed', 'phone_number')

