from rest_framework.viewsets import ModelViewSet

from .serializers import InstanceSerializer
from core.models.instance import Instance


class InstanceViewSet(ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
