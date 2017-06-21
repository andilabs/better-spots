
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api2.opinions.serializers import OpinionSerializer
from core.models.ratings import Rating
from core.models.spots import Spot


class RatingSerializer(serializers.ModelSerializer):
    opinion = OpinionSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = (
            "pk",
            "created_at",
            "updated_at",
            'is_enabled',
            'friendly_rate',
            'opinion',
        )


class ObjectInUserContextMixin(object):
    def validate(self, attrs):
        attrs['user_id'] = self.context['view'].kwargs['user_pk']
        return attrs


class UsersRatingSerializer(ObjectInUserContextMixin, RatingSerializer):

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('spot', )


class ObjectInSpotContextMixin(object):
    def validate(self, attrs):
        attrs['spot'] = Spot.objects.get(pk=self.context['view'].kwargs['spot_pk'])
        return attrs


class SpotsRatingSerializer(ObjectInSpotContextMixin, RatingSerializer):

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('user', )

    def create(self, validated_data):
        model_class = self.Meta.model
        obj, created = model_class.objects.get_or_create(
            spot=validated_data.get('spot'),
            user=validated_data.get('user'),
            defaults=validated_data)
        if not created:
            raise ValidationError('Already rated by this user')
        return obj
