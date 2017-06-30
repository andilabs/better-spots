from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from api2.permissions import IsOwnerOrReadOnly
from api2.ratings.serializers import UsersRatingSerializer, SpotsRatingSerializer
from core.models.ratings import Rating


class SpotsRatingViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Rating.objects.order_by('-pk')
    serializer_class = SpotsRatingSerializer

    def get_queryset(self):
        return super(SpotsRatingViewSet, self).get_queryset().filter(
            spot=self.kwargs['spot_pk']
        )


class UserRatingViewSet(ModelViewSet):
    queryset = Rating.objects.order_by('-pk')
    serializer_class = UsersRatingSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return super(UserRatingViewSet, self).get_queryset().filter(
            user=self.kwargs['user_pk']
        )
