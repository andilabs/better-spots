# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta


from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    authentication_classes, permission_classes, api_view
)
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
)
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from core.models import (
    Spot, Rating, UsersSpotsList
)
from accounts.models import SpotUser
from accounts.authentication import ExpiringTokenAuthentication
from .serializers import (
    SpotUserSerializer,
    SpotListSerializer,
    SpotDetailSerializer,
    SpotWithDistanceSerializer,
    PaginetedSpotWithDistanceSerializer,
    RatingSerializer,
    FavouritesSpotsListSerializer,
)
from .permissions import (
    IsOwnerOrReadOnly,
    IsAdmin
)
from utils.img_path import get_image_path


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'SPOTS': {
            'Spots': reverse(
                'spot-list', request=request),

            'Certificated Spots': reverse(
                'certificated-spot-list', request=request),

            'User favourites Spots': reverse(
                'user-favourites-spot-list', request=request),
        },
        'NEARBY': {
            'with default radius': reverse(
                'nearby_spots', request=request, kwargs={
                    'lat': 52.22642,
                    'lng': 20.98283}),

            'with default radius and paginated by {5}':
            "%s?paginated=5" % reverse(
                'nearby_spots', request=request, kwargs={
                    'lat': 52.22642,
                    'lng': 20.98283}),


            'with specified radius': reverse(
                'nearby_spots_with_radius', request=request, kwargs={
                    'lat': 52.22642,
                    'lng': 20.98283,
                    'radius': 8000}),

            'with specified radius and paginated by {5}':
            "%s?paginated=5" % reverse(
                'nearby_spots_with_radius', request=request, kwargs={
                    'lat': 52.22642,
                    'lng': 20.98283,
                    'radius': 8000}),
            },
        'Ratings': reverse(
            'rating-list', request=request),

        'Image upload to spot POST': reverse(
            'image_upload', request=request, kwargs={'pk': 2}
        ),

        'Authentication POST': reverse(
            'authentication', request=request,
        ),

        'Users (admin only)': reverse(
            'users-list', request=request,
        )
    })


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, pk):
        spot = Spot.objects.get(pk=pk)
        up_file = request.FILES['file']
        generated_filename = get_image_path()
        spot.venue_photo = default_storage.save(
            generated_filename, ContentFile(up_file.read()))
        spot.save()

        return Response({'file_url': spot.thumbnail_venue_photo}, status=201)


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAdmin, ))
class SpotUserList(ListCreateAPIView):
    serializer_class = SpotUserSerializer

    def get_queryset(self):
        queryset = SpotUser.objects.all()
        return queryset


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAdmin, ))
class SpotUserDetail(RetrieveUpdateDestroyAPIView):
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
@permission_classes((IsAuthenticated, ))
class UserFavouritesSpotsList(ListCreateAPIView):
    model = UsersSpotsList
    serializer_class = FavouritesSpotsListSerializer

    def get_queryset(self):
        queryset = UsersSpotsList.objects.filter(
            user=self.request.user,
            role=1)
        return queryset

    def post(self, request):
        user = request.user
        spot = get_object_or_404(Spot, pk=request.data.get('spot_pk'))
        role = 1

        if not UsersSpotsList.objects.filter(user=user, spot=spot, role=role):
            obj = UsersSpotsList.objects.create(
                user=user,
                spot=spot,
                role=role,
            )
            return Response({
                'detail': ("Added %s to favourites" % obj.spot.name),
                'pk': obj.pk}, status=201)

        return Response({
            'detail': 'This spot is already in your favourites'}, status=200)


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsOwnerOrReadOnly, ))
class UserFavouritesSpotDetail(RetrieveUpdateDestroyAPIView):
    model = UsersSpotsList
    serializer_class = FavouritesSpotsListSerializer

    def get_queryset(self):
        queryset = UsersSpotsList.objects.filter(
            role=1)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            role=1)
        self.check_object_permissions(self.request, obj)
        return obj


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class SpotList(ListCreateAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.filter(
            is_accepted=True,
            friendly_rate__gte=1.0,
        )
        return queryset


class CertificatedSpotList(ListAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.filter(
            is_certificated=True,
            friendly_rate__gte=1.0,
        )
        return queryset


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
class RatingList(ListCreateAPIView):
    model = Rating
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()
        return queryset

    def post(self, request):
        spot = get_object_or_404(Spot, pk=request.data.get('spot_pk'))
        user = request.user
        is_enabled = request.data.get('is_enabled', False)
        friendly_rate = request.data.get('friendly_rate')
        facilities = request.data.get('facilities')

        obj, created = Rating.objects.get_or_create(
            spot=spot, user=user, defaults={
                'friendly_rate': friendly_rate,
                'is_enabled': is_enabled,
            })

        if not created:
            obj.friendly_rate = friendly_rate
            obj.is_enabled = is_enabled

        if not obj.facilities:
            obj.facilities = {}

        for k, v in facilities.items():
            obj.facilities[k] = v

        obj.save()

        spot_ratings = [r.friendly_rate
                        for r in Rating.objects.filter(spot=spot)]

        return Response({
            'detail': '%s Rating' % ('Created' if created else 'Updated'),
            'new_score': sum(spot_ratings)/float(len(spot_ratings))
            }, status=200)


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminUser))
class RatingDetail(RetrieveUpdateDestroyAPIView):

    model = Rating
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@authentication_classes((ExpiringTokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminUser))
class SpotDetail(RetrieveUpdateDestroyAPIView):

    model = Spot
    serializer_class = SpotDetailSerializer

    def get_queryset(self):
        queryset = Spot.objects.filter(is_accepted=True)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


@api_view(http_method_names=['GET'])
def nearby_spots(request, lat=None, lng=None, radius=5000, limit=50):

    user_location = fromstr("POINT(%s %s)" % (lng, lat))
    desired_radius = {'m': radius}
    nearby_spots = Spot.objects.filter(
        friendly_rate__gte=1.0,
        is_accepted=True,
        location__distance_lte=(
            user_location,
            D(**desired_radius)
        )
    ).distance(user_location).order_by('distance')[:limit]

    paginated = request.QUERY_PARAMS.get('paginated')

    if paginated:

        try:
            paginated = int(paginated)
        except:
            paginated = settings.MAX_SPOTS_PER_PAGE_API

        paginator = Paginator(nearby_spots, paginated)
        page = request.QUERY_PARAMS.get('page')
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
        serializer = PaginetedSpotWithDistanceSerializer(
            result, context={'request': request})
    else:
        serializer = SpotWithDistanceSerializer(
            nearby_spots, many=True, context={'request': request})

    return Response(serializer.data)


@api_view(http_method_names=['POST'])
@csrf_exempt
def authentication(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        time_now = datetime.now()

        if user and user.is_active:

                token, created = Token.objects.get_or_create(user=user)

                if not created and token.created < time_now - timedelta(
                        hours=settings.TOKEN_EXPIRES_AFTER):

                    token.delete()
                    token = Token.objects.create(user=user)
                    token.created = datetime.now()
                    token.save()

                return HttpResponse(
                    json.dumps({'token': token.key}),
                    content_type="application/json; charset=UTF-8")

        else:
            return Response('Unauthorized', status=401)
