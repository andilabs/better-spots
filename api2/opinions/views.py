from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api2.opinions.serializers import OpinionSerializer
from api2.permissions import IsOwnerOrReadOnly
from core.models.opinions import Opinion


class OpinionViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Opinion.objects.order_by('-pk')
    serializer_class = OpinionSerializer


    def get_queryset(self):
        return super(OpinionViewSet, self).get_queryset().filter(
            rating=self.kwargs['rate_pk'],
            rating__spot=self.kwargs['spot_pk']
        )


class UserOpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.order_by('-pk')
    serializer_class = OpinionSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    object_user_to_check = 'rating.user'

    def get_queryset(self):
        return super(UserOpinionViewSet, self).get_queryset().filter(
            rating=self.kwargs['rate_pk'],
            rating__user=self.kwargs['user_pk']
        )
