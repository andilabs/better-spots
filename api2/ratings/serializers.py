from rest_framework import serializers

from api2.opinions.serializers import OpinionSerializer
from core.models.ratings import Rating


class RatingSerializer(serializers.ModelSerializer):
    opinion = OpinionSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = [
            "pk",
            "created_at",
            "updated_at",
            'is_enabled',
            'friendly_rate',
            'user',
            'spot',
            'opinion',
        ]
