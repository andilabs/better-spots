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
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


from core.models import Spot, Rating, Opinion, OpinionUsefulnessRating, UsersSpotsList
from accounts.models import SpotUser
from .serializers import (
    SpotUserSerializer,
    SpotListSerializer, SpotDetailSerializer,
    PaginetedSpotWithDistanceSerializer,
    RatingSerializer,
    FavouritesSpotsListSerializer,
)
from accounts.authentication import ExpiringTokenAuthentication

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from utils.img_path import get_image_path


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, pk):
        spot = Spot.objects.get(pk=pk)
        up_file = request.FILES['file']
        generated_filename = get_image_path()

        spot.venue_photo = default_storage.save(generated_filename, ContentFile(up_file.read()))
        spot.save()

        return Response({'file_url': spot.thumbnail_venue_photo}, status=201)


@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotUserList(generics.ListCreateAPIView):
    serializer_class = SpotUserSerializer

    def get_queryset(self):
        queryset = SpotUser.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, ))
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


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
class UserFavouritesSpotsList(generics.ListCreateAPIView):
    model = UsersSpotsList
    serializer_class = FavouritesSpotsListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UsersSpotsList.objects.filter(user=self.request.user, role=1)
        return queryset

    def post(self, request):
        user = request.user
        spot = get_object_or_404(Spot, pk=request.data.get('spot_pk'))
        role = 1 #for now just hardcoded favourites

        if not UsersSpotsList.objects.filter(user=user, spot=spot, role=role):
            o = UsersSpotsList.objects.create(
                user=user,
                spot=spot,
                role=role,
            )
            return Response({
                'detail': ("Added %s to favourites" % o.spot.name),
                'pk': o.pk}, status=201)
        return Response({'detail': 'This spot is already in your favourites'}, status=200)


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
class UserFavouritesSpotDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UsersSpotsList
    serializer_class = FavouritesSpotsListSerializer

    def get_queryset(self):
        queryset = UsersSpotsList.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotList(generics.ListCreateAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class RatingList(generics.ListCreateAPIView):
    model = Rating
    serializer_class = RatingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Rating.objects.all()
        return queryset

    def post(self, request):
        spot = get_object_or_404(Spot, pk=request.data.get('spot_pk'))
        user = request.user
        is_enabled = request.data.get('is_enabled', False)
        friendly_rate = request.data.get('friendly_rate')
        facilities = request.data.get('facilities')

        obj, created = Rating.objects.get_or_create(spot=spot, user=user, defaults={
            'friendly_rate': friendly_rate,
            'is_enabled': is_enabled,
            })
        if not created:
            obj.friendly_rate = friendly_rate
            obj.is_enabled = is_enabled

        if facilities:
            for k,v in facilities.items():
                obj.facilities[k] = v
        obj.save()

        spot_ratings = [r.friendly_rate for r in Rating.objects.filter(spot=spot)]

        return Response({
            'detail': '%s Rating' % ('Created' if created else 'Updated'),
            'new_score': sum(spot_ratings)/float(len(spot_ratings))
            }, status=200)


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminUser))
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Rating
    serializer_class = RatingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Rating.objects.all()
        return queryset

    def get_object(self):
        user = self.request.user
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminUser))
class SpotDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    * Provides `get`, `put`, `patch` and `delete` method handlers.
    * Requires `token authentication` for modifing methods.



    Example request:

        curl -X DELETE http://127.0.0.1:8000/api/spots/2/ -H 'Authorization: Token 299dc186f3d3f113921b4555b3c22a197d1da254'

    """

    model = Spot
    serializer_class = SpotDetailSerializer

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

    paginator = Paginator(nearby_spots, settings.MAX_SPOTS_PER_PAGE)

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
        docs/build/html/api.html#post--api-authentication

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