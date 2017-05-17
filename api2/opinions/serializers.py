from rest_framework import serializers

from core.models.opinions import Opinion


class OpinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opinion
        fields = '__all__'
