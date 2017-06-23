from rest_framework import serializers

from accounts.models import User, UserFavouritesSpotList
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


class UsersFavouritesSpotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFavouritesSpotList
        fields = [
            "id",
            "user",
            "spot",
        ]
