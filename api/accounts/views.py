from rest_framework.viewsets import ModelViewSet
from rest_framework.reverse import reverse

from accounts.models import User, UserFavouritesSpotList
from api.permissions import IsOwnerOrReadOnly
from api.accounts.serializers import UserSerializer, UsersFavouritesSpotsSerializer


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

    def create(self, request, *args, **kwargs):
        response = super(UserFavouritesSpotsViewSet, self).create(request, args, kwargs)
        response.data['url'] = reverse(
            'api:user-favourites-detail',
            kwargs={'user_pk': self.request.user.pk, 'pk': response.data['id']}
        )
        return response
