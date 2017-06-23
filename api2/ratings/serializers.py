
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api2.accounts.mixins import ObjectInUserContextMixin
from api2.opinions.serializers import OpinionSerializer
from api2.spots.mixins import ObjectInSpotContextMixin
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


class UsersRatingSerializer(ObjectInUserContextMixin, RatingSerializer):

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('spot', )


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
