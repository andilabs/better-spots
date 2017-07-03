
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import User
from api2.accounts.mixins import ObjectInUserContextMixin
from api2.opinions.serializers import OpinionSerializer
from api2.spots.mixins import ObjectInSpotContextMixin
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
        return validated_data


class SpotsRatingSerializer(ObjectInSpotContextMixin, RatingSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.none())

    class Meta(RatingSerializer.Meta):
        model = Rating
        fields = RatingSerializer.Meta.fields + ('user', )

    def validate(self, attrs):
        validated_data = super(SpotsRatingSerializer, self).validate(attrs)
        if Rating.objects.filter(spot=validated_data['spot'], user=validated_data['user']).exists():
            raise ValidationError('Already rated by this user')
        return validated_data

    def __init__(self, *args, **kwargs):
        super(SpotsRatingSerializer, self).__init__(*args, **kwargs)
        if hasattr(self.context['request'].user, 'pk'):
            self.fields['user'].queryset = User.objects.filter(pk=self.context['request'].user.pk)
