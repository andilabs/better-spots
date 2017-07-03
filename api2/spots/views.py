from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from api2.spots.filtersets import SpotFilterSet
from api2.spots.serializers import SpotSerializer
from core.models.spots import Spot


class SpotViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):

    queryset = Spot.objects.order_by('pk')
    serializer_class = SpotSerializer
    filter_class = SpotFilterSet
    permission_classes = (IsAuthenticatedOrReadOnly, )
