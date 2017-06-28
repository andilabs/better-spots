from rest_framework.viewsets import ModelViewSet

from accounts.models import User, UserFavouritesSpotList
from api2.permissions import IsOwnerOrReadOnly
from api2.accounts.serializers import UserSerializer, UsersFavouritesSpotsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('pk').prefetch_related('favourites')
    serializer_class = UserSerializer


class UserFavouritesSpotsViewSet(ModelViewSet):
    queryset = UserFavouritesSpotList.objects.order_by('-pk')
    serializer_class = UsersFavouritesSpotsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return super(UserFavouritesSpotsViewSet, self).get_queryset().filter(
            user=self.kwargs['user_pk']
        )
