from rest_framework.viewsets import ModelViewSet

from api2.ratings.serializers import UsersRatingSerializer, SpotsRatingSerializer
from core.models.ratings import Rating


class SpotsRatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = SpotsRatingSerializer

    def get_queryset(self):
        return super(SpotsRatingViewSet, self).get_queryset().filter(
            spot=self.kwargs['spot_pk']
        )


class UserRatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = UsersRatingSerializer

    def get_queryset(self):
        return super(UserRatingViewSet, self).get_queryset().filter(
            user=self.kwargs['user_pk']
        )
