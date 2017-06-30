from rest_framework import serializers

from core.models.opinions import Opinion


class OpinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opinion
        fields = [
            "pk",
            "created_at",
            "updated_at",
            "opinion_text",
        ]
