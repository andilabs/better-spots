from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api2.opinions.serializers import OpinionSerializer
from core.models.opinions import Opinion


class OpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

    def list(self, request, spot_pk=None, rate_pk=None):
        queryset = Opinion.objects.filter(rating__spot=spot_pk, rating=rate_pk)
        serializer = OpinionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, spot_pk=None, rate_pk=None):
        queryset = Opinion.objects.filter(pk=pk, rating__spot=spot_pk, rating=rate_pk)
        opinion = get_object_or_404(queryset, pk=pk)
        serializer = OpinionSerializer(opinion)
        return Response(serializer.data)


class UserOpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

    def list(self, request, user_pk=None, rate_pk=None):
        queryset = Opinion.objects.filter(rating__user=user_pk, rating=rate_pk)
        serializer = OpinionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, rate_pk=None):
        queryset = Opinion.objects.filter(pk=pk, rating__user=user_pk, rating=rate_pk)
        opinion = get_object_or_404(queryset, pk=pk)
        serializer = OpinionSerializer(opinion)
        return Response(serializer.data)