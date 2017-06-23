from rest_framework.viewsets import ModelViewSet

from api2.spots.filtersets import SpotFilterSet
from api2.spots.serializers import SpotSerializer
from core.models.spots import Spot


class SpotViewSet(ModelViewSet):

    queryset = Spot.objects.order_by('pk')
    serializer_class = SpotSerializer
    filter_class = SpotFilterSet

