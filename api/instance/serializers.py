from rest_framework import serializers

from core.models.instance import Instance


class InstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instance
        fields = '__all__'
