from rest_framework.viewsets import ModelViewSet

from .serializers import OpinionSerializer
from core.models.opinions import Opinion


class OpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
