from django.contrib.gis.geos.point import Point
from factory import django, fuzzy
from faker import Factory

from core.models.spots import SPOT_TYPE_CHOICES

import random
from django.contrib.gis.geos import Point
from factory.fuzzy import BaseFuzzyAttribute

faker = Factory.create('pl_PL')

class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(
            random.uniform(20.983331, 21.071981),
            random.uniform(52.2110206, 52.216912)
        )


class SpotFactory(django.DjangoModelFactory):
    spot_type = fuzzy.FuzzyChoice(dict(SPOT_TYPE_CHOICES).keys())
    location = FuzzyPoint()

    class Meta:
        model = 'core.Spot'

    name = fuzzy.FuzzyText(length=32, chars='0123456789abcdef')
    address_city = faker.city()
    address_country = faker.country()

    # @classmethod
    # def _generate(cls, create, attrs):
    #     lat = fuzzy.FuzzyFloat(52.2110206, 52.216912)
    #     lon = fuzzy.FuzzyFloat(20.983331, 21.071981)
    #
    #     spot =  super(SpotFactory, cls)._generate(create, attrs)
    #     import ipdb; ipdb.set_trace()
    #     spot.location = Point(lat, lon)
    #     return spot