import random

from django.contrib.gis.geos import Point
from factory import django, fuzzy, lazy_attribute
from faker import Factory

from core.models.spots import SPOT_TYPE_CHOICES
from utils.geocoding import reverse_geocoding


faker = Factory.create('pl_PL')


class FuzzyPoint(fuzzy.BaseFuzzyAttribute):

    def fuzz(self):
        return Point(
            random.uniform(20.961733, 21.071981),
            random.uniform(52.167108, 52.216912)
        )
        # TODO more sexy approach for given point get random points within radius
        # https://gis.stackexchange.com/questions/25877/generating-random-locations-nearby/68275


class SpotFactory(django.DjangoModelFactory):
    spot_type = fuzzy.FuzzyChoice(dict(SPOT_TYPE_CHOICES).keys())
    location = FuzzyPoint()

    class Meta:
        model = 'core.Spot'

    is_accepted = True
    is_enabled = fuzzy.FuzzyChoice([True, False])
    friendly_rate = fuzzy.FuzzyDecimal(0.0, 5.0, 2)

    @lazy_attribute
    def name(self):
        return "{type} '{name}'".format(
            type=dict(SPOT_TYPE_CHOICES)[self.spot_type],
            name=faker.first_name()
        )

    @classmethod
    def _generate(cls, create, attrs):
        # TODO parametrize this factory, so that using google api is an option not default
        spot = super(SpotFactory, cls)._generate(create, attrs)
        longitude, latitude = spot.location.coords
        address_info = reverse_geocoding(latitude=latitude, longitude=longitude)
        spot.address_number = address_info.get('address_number')
        spot.address_street = address_info.get('address_street')
        spot.address_city = address_info.get('address_city')
        spot.address_country = address_info.get('address_country')
        spot.save()
        return spot
