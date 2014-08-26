from rest_framework import serializers
from demo.models import (
    Spot, Rating, Opinion, OpinionUsefulnessRating, DogspotUser, OtoFoto)


class OtoFotoSerializer(serializers.HyperlinkedModelSerializer):
    obrazek_full = serializers.Field()

    class Meta:
        model = OtoFoto
        fields = ('url', 'obrazek', 'obrazek_full')


class DogspotUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DogspotUser
        fields = ('url', 'mail_verified', 'email')


class OpinionUsefulnessRatingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='opinion-detail')
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='dogspotuser-detail')

    class Meta:
        model = OpinionUsefulnessRating
        fields = ('url', 'opinion', 'vote', 'user')


class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    rating = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='rating-detail')
    opinion_usefulnes_ratings = OpinionUsefulnessRatingSerializer(
        read_only=True)

    class Meta:
        model = Opinion
        fields = (
            'opinion_text', 'url', 'rating', 'opinion_usefulnes_ratings')


class RatingSerializer(serializers.HyperlinkedModelSerializer):

    opinion = OpinionSerializer(many=False, read_only=True)
    spot = serializers.HyperlinkedRelatedField(
        many=False, read_only=False, view_name='spot-detail')
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=False, view_name='dogspotuser-detail')
    dogs_allowed = serializers.BooleanField()

    class Meta:
        model = Rating
        fields = (
            'url', 'dogs_allowed', 'friendly_rate', 'spot', 'opinion', 'user')


class SpotListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Spot


class SpotDetailSerializer(SpotListSerializer):

    ratings = RatingSerializer(read_only=True)

    class Meta:
        model = Spot


class SpotWithDistanceSerializer(SpotListSerializer):
    id = serializers.Field()
    distance = serializers.Field()

    class Meta:
        model = Spot
