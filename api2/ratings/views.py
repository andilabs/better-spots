from rest_framework.viewsets import ModelViewSet

from .serializers import RatingSerializer
from core.models.ratings import Rating


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
