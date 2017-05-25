from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from api2.accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request, spot_pk=None, rate_pk=None):
    #     queryset = User.objects.filter(rating__spot=spot_pk, rating=rate_pk)
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None, spot_pk=None, rate_pk=None):
    #     queryset = User.objects.filter(pk=pk, rating=rate_pk)
    #     opinion = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(opinion)
    #     return Response(serializer.data)
