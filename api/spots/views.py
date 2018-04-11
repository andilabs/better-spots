from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from api.spots.filtersets import SpotFilterSet, SpotFullTextSearchFilterSet
from api.spots.serializers import SpotSerializer
from core.models.spots import Spot
from utils.search import spots_full_text_search


class SpotViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):

    queryset = Spot.objects.order_by('pk')
    serializer_class = SpotSerializer
    filter_class = SpotFilterSet
    permission_classes = (IsAuthenticatedOrReadOnly, )


class SpotSearchView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = SpotSerializer
    filter_class = SpotFullTextSearchFilterSet
    queryset = Spot.objects.order_by('pk')
