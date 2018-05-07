from collections import namedtuple
from rest_framework import serializers

from django.contrib.gis.geos.point import Point

GeoPoint = namedtuple('GeoPoint', ['longitude', 'latitude'])


class GeoPointSerializerField(serializers.Field):
    """This field expects on creation data in format like these:
    {
        "latitude" 25.024444,
        "longitude": 55.2323232
    }

    """

    def to_representation(self, value):
        """ returns dict like
        {
            "latitude" 25.024444,
            "longitude": 55.2323232
        }
        :param value: Point
        :type value: models.PointField
        :return: dict with latitude and longitude keys
        ":rtype: dict
        """
        geo = GeoPoint(*value.coords)
        return geo._asdict()

    def to_internal_value(self, data):
        """unpacks dict and maps it onto namedtuple GeoPoint and after
        casting to floats returns valid django.contrib.gis.geos.point.Point

        :param data: dict with latitude and longitude keys
        :return: Point object
        :rtype: django.contrib.gis.geos.point.Point
        """
        if not isinstance(data, dict):
            data = eval(data)
        geo = GeoPoint(**data)
        return Point(*[float(i) for i in geo])
