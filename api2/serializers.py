from collections import namedtuple
from rest_framework import serializers

from django.contrib.gis.geos.point import Point


GeoPoint = namedtuple('GeoPoint', ['longitude', 'latitude'])

class GeoPointSerializerField(serializers.Field):

    def to_representation(self, obj):
        geo = GeoPoint(*obj.coords)
        return geo._asdict()

    def to_internal_value(self, data):
        geo = GeoPoint(**data)
        return Point(*geo)
