
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from api.accounts.mixins import ObjectInUserContextMixin
from api.opinions.serializers import OpinionSerializer
from api.spots.mixins import ObjectInSpotContextMixin
from core.models.ratings import Rating


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
            'tags',
        )


class UsersRatingSerializer(ObjectInUserContextMixin, RatingSerializer):

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('spot', )

    def validate(self, attrs):
        validated_data = super(UsersRatingSerializer, self).validate(attrs)
        if Rating.objects.filter(spot=validated_data['spot'], user=validated_data['user']).exists():
            raise ValidationError('Already rated by this user')
        if validated_data['user'] != self.context['request'].user:
            raise PermissionDenied
        return validated_data


class SpotsRatingSerializer(ObjectInSpotContextMixin, RatingSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('user', )

    def create(self, validated_data):
        obj, created = Rating.objects.update_or_create(
            spot=validated_data['spot'], user=self.context['request'].user,
            defaults=validated_data
        )
        return obj
