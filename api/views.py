# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta


from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


from core.models import Spot, Raiting, Opinion, OpinionUsefulnessRating
from accounts.models import SpotUser
from .serializers import (
    SpotUserSerializer,
    SpotListSerializer, SpotDetailSerializer,
    PaginetedSpotWithDistanceSerializer,
    RaitingSerializer,
    OpinionSerializer,
    OpinionUsefulnessRatingSerializer
    )
from accounts.authentication import ExpiringTokenAuthentication

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from utils.img_path import get_image_path


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        spot = Spot.objects.get(pk=1)
        up_file = request.FILES['file']
        generated_filename = get_image_path()

        spot.venue_photo = default_storage.save(generated_filename, ContentFile(up_file.read()))
        spot.save()

        return Response({'file_url': spot.thumbnail_venue_photo}, status=201)


# @authentication_classes((ExpiringTokenAuthentication, ))
# @permission_classes((IsAuthenticatedOrReadOnly,))
class SpotUserList(generics.ListCreateAPIView):
    serializer_class = SpotUserSerializer

    def get_queryset(self):
        queryset = SpotUser.objects.all()
        return queryset


# @authentication_classes((ExpiringTokenAuthentication, ))
# @api_view(http_method_names=['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = SpotUser
    serializer_class = SpotUserSerializer

    def get_queryset(self):
        queryset = SpotUser.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotList(generics.ListCreateAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class OpinionUsefulness(generics.RetrieveUpdateDestroyAPIView):
    model = OpinionUsefulnessRating
    serializer = OpinionUsefulnessRatingSerializer

    def get_queryset(self):
        queryset = Opinion.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class OpinionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Opinion
    serializer_class = OpinionSerializer

    def get_queryset(self):
        queryset = Opinion.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class RaitingList(generics.ListCreateAPIView):
    model = Raiting
    serializer_class = RaitingSerializer

    def get_queryset(self):
        queryset = Raiting.objects.all()
        return queryset


class RaitingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Raiting
    serializer_class = RaitingSerializer

    def get_queryset(self):
        queryset = Raiting.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    * Provides `get`, `put`, `patch` and `delete` method handlers.
    * Requires `token authentication` for modifing methods.



    Example request:

        curl -X DELETE http://127.0.0.1:8000/api/spots/2/ -H 'Authorization: Token 299dc186f3d3f113921b4555b3c22a197d1da254'

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
def nearby_spots(request, lat=None, lng=None, radius=5000, limit=50):

    if not lat and not lng:
        return HttpResponseRedirect(reverse('nearby_spots', kwargs={'lat': 52.22805, 'lng': 21.00208}))

    user_location = fromstr("POINT(%s %s)" % (lng, lat))
    desired_radius = {'m': radius}
    nearby_spots = Spot.objects.filter(location__distance_lte=(user_location, D(**desired_radius))).distance(user_location).order_by('distance')[:limit]

    paginator = Paginator(nearby_spots, 15)

    page = request.QUERY_PARAMS.get('page')

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    serializer = PaginetedSpotWithDistanceSerializer(
        result, context={'request': request})

    return Response(serializer.data)

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