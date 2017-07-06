from collections import namedtuple
from rest_framework import serializers

from django.contrib.gis.geos.point import Point


GeoPoint = namedtuple('GeoPoint', ['longitude', 'latitude'])

# TODO try using type NamedTuple like this
# from typing import NamedTuple
# GeoPoint = NamedTuple('GeoPoint', [('longitude', float), ('latitude', float)])
# TODO so the cast in to_internal_value won't be needed
# or use enforce so it will crash when passed not proper type
# https://github.com/RussBaz/enforce

class GeoPointSerializerField(serializers.Field):

    def to_representation(self, obj):
        geo = GeoPoint(*obj.coords)
        return geo._asdict()

    def to_internal_value(self, data):
        geo = GeoPoint(**data)
        return Point(*[float(i) for i in geo])
