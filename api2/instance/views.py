from rest_framework.viewsets import ModelViewSet

from api2.instance.serializers import InstanceSerializer
from core.models.instance import Instance


class InstanceViewSet(ModelViewSet):
    queryset = Instance.objects.get()
    serializer_class = InstanceSerializer
