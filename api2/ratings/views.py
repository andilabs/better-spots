from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api2.ratings.serializers import RatingSerializer
from core.models.ratings import Rating


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def list(self, request, spot_pk=None):
        queryset = Rating.objects.filter(spot=spot_pk)
        serializer = RatingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, spot_pk=None):
        queryset = Rating.objects.filter(pk=pk, spot=spot_pk)
        rating = get_object_or_404(queryset, pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)


class UserRatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def list(self, request, user_pk=None):
        queryset = Rating.objects.filter(user=user_pk)
        serializer = RatingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = Rating.objects.filter(pk=pk, user=user_pk)
        rating = get_object_or_404(queryset, pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)