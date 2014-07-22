from rest_framework import serializers
from demo.models import Spot, Raiting, Opinion, OpinionUsefulnessRating, DogspotUser, OtoFoto


class OtoFotoSerializer(serializers.HyperlinkedModelSerializer):
    obrazek_full = serializers.Field()

    class Meta:
        model = OtoFoto
        fields = ('url','obrazek','obrazek_full')

class DogspotUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DogspotUser
        fields = ('url', 'mail_sent', 'email')


class OpinionUsefulnessRatingSerializer(serializers.HyperlinkedModelSerializer):
    opinion = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='opinion-detail')
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='dogspotuser-detail')

    class Meta:
        model = OpinionUsefulnessRating
        fields = ('url', 'opinion', 'vote', 'user')


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
        many=False, read_only=False, view_name='spot-detail')
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=False, view_name='dogspotuser-detail')

    class Meta:
        model = Raiting
        fields = (
            'url', 'dogs_allowed', 'friendly_rate', 'spot', 'opinion', 'user')


class SpotListSerializer(serializers.HyperlinkedModelSerializer):

    friendly_rate = serializers.Field()
    dogs_allowed = serializers.Field()

    class Meta:
        model = Spot


class SpotDetailSerializer(SpotListSerializer):

    raitings = RaitingSerializer(read_only=True)

    class Meta:
        model = Spot


class SpotWithDistanceSerializer(SpotListSerializer):
    id = serializers.Field()
    distance = serializers.Field()

    class Meta:
        model = Spot

# class SpotWithDistanceSerializer(serializers.HyperlinkedModelSerializer):
#     distance = serializers.Field()
#     friendly_rate = serializers.Field()
#     dogs_allowed = serializers.Field()

#     class Meta:
#         model = Spot
#         fields = (
#             'id', 'distance', 'url', 'name', 'latitude', 'longitude',
#             'address_street', 'address_number', 'address_city',
#             'address_country', 'spot_type', 'is_accepted', 'friendly_rate',
#             'dogs_allowed', 'phone_number')