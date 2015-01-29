# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta


from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.json_response import JSONResponse
from core.models import Spot, Raiting, Opinion, OpinionUsefulnessRating
from accounts.models import SpotUser
from .serializers import (
    SpotUserSerializer,
    SpotListSerializer, SpotDetailSerializer, PaginetedSpotWithDistanceSerializer,
    RaitingSerializer,
    OpinionSerializer,
    OpinionUsefulnessRatingSerializer
    )
from accounts.authentication import ExpiringTokenAuthentication


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
class SpotUserList(generics.ListCreateAPIView):
    serializer_class = SpotUserSerializer

    def get_queryset(self):
        queryset = SpotUser.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
class SpotUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = SpotUser
    serializer_class = SpotUserSerializer


# @authentication_classes((ExpiringTokenAuthentication, ))
# @permission_classes((IsAuthenticated,))
class SpotList(generics.ListCreateAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
class OpinionUsefulness(generics.RetrieveUpdateDestroyAPIView):
    model = OpinionUsefulnessRating
    serializer = OpinionUsefulnessRatingSerializer


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
class OpinionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Opinion
    serializer_class = OpinionSerializer


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
class RaitingList(generics.ListCreateAPIView):
    model = Raiting
    serializer_class = RaitingSerializer

    def get_queryset(self):
        queryset = Raiting.objects.all()
        return queryset


class RaitingDetail(RaitingList):
    model = Raiting
    serializer_class = RaitingSerializer

    def get_queryset(self):
        queryset = Raiting.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


class SpotDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    * Requires `token authentication`
    * Only `admin` users are able to access this view.


        EXAMPLE CALL:

            curl -X GET http://127.0.0.1:8000/api/spots/2/ -H 'Authorization: Token 299dc186f3d3f113921b4555b3c22a197d1da254'

    """

    model = Spot
    serializer_class = SpotDetailSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Spot.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@api_view(http_method_names=['GET'])
def nearby_spots(request, lat, lng, radius=5000, limit=50):

    user_location = fromstr("POINT(%s %s)" % (lng, lat))
    desired_radius = {'m': radius}
    nearby_spots = Spot.objects.filter(location__distance_lte=(user_location, D(**desired_radius))).distance(user_location).order_by('distance')[:limit]

    paginator = Paginator(nearby_spots, 5)

    page = request.QUERY_PARAMS.get('page')
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}

    serializer = PaginetedSpotWithDistanceSerializer(
        result,
        context=serializer_context
        )

    return Response(serializer.data)

    # serializer = SpotWithDistanceSerializer(nearby_spots, many=True)
    # return Response(serializer.data)


@api_view(http_method_names=['GET',  'POST'])
@csrf_exempt
def authentication(request):
    """
    Method is responsible to provide TOKEN
    to sucessfully authenticated user


    Following parameters should be passed in HTTP POST:

    `email`
    `password`

    EXAMPLE REQUEST:

        curl -X POST http://127.0.0.1:8000/api/authentication -d "email=andi@andilabs.com&password=d00r00tk@"

    EXAMPLE RESPONSE:

        {"token": "3a3f1cd20ee72b468a9bd7d6ab20e2e0a408ead5"}
    """
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        time_now = datetime.now()

        if user and user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                if not created and token.created < time_now - timedelta(
                        hours=settings.TOKEN_EXPIRES_AFTER):
                    # for comparing dates USE_TZ = False in settings
                    token.delete()
                    token = Token.objects.create(user=user)
                    token.created = datetime.now()
                    token.save()

                return HttpResponse(
                    json.dumps({'token': token.key}),
                    content_type="application/json; charset=UTF-8")

        else:
            return Response('Unauthorized', status=401)
    else:
        return  Response('Unauthorized', status=401)