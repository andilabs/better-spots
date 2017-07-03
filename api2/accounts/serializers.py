from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied
from accounts.models import User, UserFavouritesSpotList
from api2.accounts.mixins import ObjectInUserContextMixin
from api2.spots.serializers import SpotSerializer


class UserSerializer(serializers.ModelSerializer):

    favourites = SpotSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "pk",
            "email",
            "favourites",
        ]


class UsersFavouritesSpotsSerializer(ObjectInUserContextMixin, serializers.ModelSerializer):

    class Meta:
        model = UserFavouritesSpotList
        fields = [
            "id",
            "spot",
        ]

    def validate(self, attrs):
        validated_data = super(UsersFavouritesSpotsSerializer, self).validate(attrs)
        if UserFavouritesSpotList.objects.filter(spot=validated_data['spot'], user=validated_data['user']).exists():
            raise ValidationError('Already in user favourites')
        if validated_data['user'] != self.context['request'].user:
            raise PermissionDenied
        return validated_data
