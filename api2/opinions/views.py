from rest_framework.viewsets import ModelViewSet

from api2.opinions.serializers import OpinionSerializer
from core.models.opinions import Opinion


class OpinionViewSet(ModelViewSet):
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

    def get_queryset(self):
        return super(UserOpinionViewSet, self).get_queryset().filter(
            rating=self.kwargs['rate_pk'],
            rating__user=self.kwargs['user_pk']
        )
