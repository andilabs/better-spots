from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.instance.serializers import InstanceSerializer
from core.models.instance import Instance


class InstanceViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
