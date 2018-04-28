import json
import responses

from django.conf import settings
from django.contrib.gis.geos import Point
from django.test import TestCase

from accounts.factories import UserFactory
from core.factories.ratings import RatingFactory
from core.factories.spots import SpotFactory
from core.models.ratings import Rating
from core.models.spots import Spot
from utils.factories import TagFactory
from utils.geocoding import REVERSE_GEOCODING_URL
from utils.tests import RESPONSE_GEOCODING_MOCK

RESPONSE_GEOCODING_MOCK_2 = {
    'results': [
        {'address_components': [
            {'long_name': '47',
              'short_name': '47',
              'types': ['street_number']},
             {'long_name': 'Kolejowa',
              'short_name': 'Kolejowa',
              'types': ['route']},
             {'long_name': 'Wola',
              'short_name': 'Wola',
              'types': ['political',
                        'sublocality',
                        'sublocality_level_1']},
             {'long_name': 'Warszawa',
              'short_name': 'Warszawa',
              'types': ['locality', 'political']},
             {'long_name': 'Warszawa',
              'short_name': 'Warszawa',
              'types': ['administrative_area_level_2',
                        'political']},
             {'long_name': 'mazowieckie',
              'short_name': 'mazowieckie',
              'types': ['administrative_area_level_1',
                        'political']},
             {'long_name': 'Poland',
              'short_name': 'PL',
              'types': ['country', 'political']},
             {'long_name': '01-210',
              'short_name': '01-210',
              'types': ['postal_code']}],
              'formatted_address': 'Kolejowa 47, 01-210 Warszawa, Poland',
              'geometry': {'bounds': {'northeast': {'lat': 52.22673450000001,
                                                    'lng': 20.9833889},
                                      'southwest': {'lat': 52.2261726,
                                                    'lng': 20.9823615}},
                           'location': {'lat': 52.2263065,
                                        'lng': 20.9828941},
                           'location_type': 'ROOFTOP',
                           'viewport': {'northeast': {'lat': 52.22780253029151,
                                                      'lng': 20.98422418029151},
                                        'southwest': {'lat': 52.22510456970851,
                                                      'lng': 20.9815262197085}}},
              'place_id': 'ChIJW6aw25vMHkcRxgIq9iMcxA8',
              'types': ['establishment', 'point_of_interest', 'premise']},
             ], 'status': 'OK'}


class RecalculatingSpotEvaluations(TestCase):

    def setUp(self):
        self.s1 = SpotFactory(name='s1')
        self.u1 = UserFactory(email='a@b.pl')
        self.u2 = UserFactory(email='c@d.pl')
        self.u3 = UserFactory(email='e@f.pl')
        self.t1 = TagFactory(text='snack')
        self.t2 = TagFactory(text='fresh_water')
        self.t3 = TagFactory(text='dedicated_menu')

    def test_rating_is_updated_correctly(self):
        """check average friendly_rate for spot is properly re-calculated"""
        RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1)
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        # single rate
        self.assertEqual(s1_from_db.friendly_rate, 1)

        RatingFactory(friendly_rate=5, spot=self.s1, user=self.u2)
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        # after another rate
        self.assertEqual(s1_from_db.friendly_rate, 3)

        Rating.objects.update_or_create(user=self.u2, spot=self.s1, defaults={
            'friendly_rate': 3
        })
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        # after user updated own rate
        self.assertEqual(s1_from_db.friendly_rate, 2)

    def test_enabled_status_is_updated_correctly(self):
        RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        self.assertEqual(s1_from_db.is_enabled, True)

        RatingFactory(friendly_rate=1, spot=self.s1, user=self.u2, is_enabled=False)
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        # still true because ratio is >= 0.5
        self.assertEqual(s1_from_db.is_enabled, True)

        Rating.objects.update_or_create(user=self.u1, spot=self.s1, defaults={
            'is_enabled': False
        })
        s1_from_db = Spot.objects.get(pk=self.s1.pk)
        # one user updated rating to True->False
        self.assertEqual(s1_from_db.is_enabled, False)

    def test_tags_are_updated_correctly_initial_state(self):
        # before any rates are added spot has no tags
        self.assertEqual(list(self.s1.tags.all()), [])

    def test_tags_are_updated_correctly(self):
        # check spot tags are updated properly after rate with tag is added
        r = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        r.tags.add(self.t1)
        self.assertEqual(list(self.s1.tags.all()), [self.t1])
        self.assertEqual(self.s1.tags.first().text, self.t1.text)

    def test_tags_are_updated_correctly_multiple_tags_added(self):
        # check spot tags are updated properly after rate with multiple tags is added
        r = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        r.tags.add(*[self.t1, self.t2])
        self.assertEqual(list(self.s1.tags.all()), [self.t1, self.t2])
        self.assertEqual(list(self.s1.tags.values_list('text', flat=True)), [self.t1.text, self.t2.text])

    def test_tags_are_updated_correctly_after_ratings_tags_cleared(self):
        # check spot tags are updated properly after rate with multiple tags is added
        r = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        r.tags.add(*[self.t1, self.t2])
        r.tags.clear()
        self.assertEqual(list(self.s1.tags.all()), [])
        self.assertEqual(list(self.s1.tags.values_list('text', flat=True)), [])

    def test_tags_are_updated_correctly_after_multiple_ratings_added(self):
        # check spot tags are updated properly after rate with multiple tags is added
        r1 = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        r1.tags.add(*[self.t1, self.t2])

        r2 = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u2, is_enabled=True)
        r2.tags.add(*[self.t2, self.t3])

        self.assertEqual(list(self.s1.tags.all()), [self.t1, self.t2, self.t3])
        self.assertEqual(list(self.s1.tags.values_list('text', flat=True)), [self.t1.text, self.t2.text, self.t3.text])

    def test_rating_update_with_new_tags_and_delete_of_previous_one(self):
        r1 = RatingFactory(friendly_rate=1, spot=self.s1, user=self.u1, is_enabled=True)
        r1.tags.add(*[self.t1, self.t2])
        r1.tags.remove(self.t1)
        r1.tags.add(self.t3)

        self.assertEqual(list(self.s1.tags.all()), [self.t2, self.t3])
        self.assertEqual(list(self.s1.tags.values_list('text', flat=True)), [self.t2.text, self.t3.text])


class AddressAndSlugUpdateWhenLocationChanges(TestCase):

    @responses.activate
    def test_address_is_set_correctly_when_new_spot_created(self):
        latitude, longitude = 52.27904, 20.980366
        responses.add(
            responses.GET,
            REVERSE_GEOCODING_URL.format(
                latitude=latitude,
                longitude=longitude,
                api_key=settings.GOOGLE_MAP_API_KEY
            ),
            body=json.dumps(RESPONSE_GEOCODING_MOCK),
            content_type="application/json"
        )
        s1 = SpotFactory(
            name='test',
            location=Point(latitude, longitude)
        )
        s1 = Spot.objects.get(pk=s1.pk)
        self.assertEqual(
            s1.address_city, 'Warszawa'
        )
        self.assertEqual(
            s1.address_street, 'Mickiewicza'
        )

    @responses.activate
    def test_slug_is_created_correctly_when_new_spot_created(self):
        latitude, longitude = 52.27904, 20.980366
        responses.add(
            responses.GET,
            REVERSE_GEOCODING_URL.format(
                latitude=latitude,
                longitude=longitude,
                api_key=settings.GOOGLE_MAP_API_KEY
            ),
            body=json.dumps(RESPONSE_GEOCODING_MOCK),
            content_type="application/json"
        )
        s1 = SpotFactory(
            name='test',
            location=Point(latitude, longitude)
        )
        s1 = Spot.objects.get(pk=s1.pk)
        self.assertEqual(
            s1.spot_slug, '{name}-{type}-{city}-{street}-{number}'.format(
                name=s1.name.lower(),
                type=s1.get_spot_type_display().lower(),
                city=s1.address_city.lower(),
                street=s1.address_street.lower(),
                number=s1.address_number.lower()
            )
        )

    @responses.activate
    def test_address_is_updated_correctly_when_spot_location_changed(self):
        latitude_1, longitude_1 = 52.226297, 20.982749
        url = REVERSE_GEOCODING_URL.format(
            latitude=latitude_1,
            longitude=longitude_1,
            api_key=settings.GOOGLE_MAP_API_KEY
        )
        responses.add(
            responses.GET,
            url,
            body=json.dumps(RESPONSE_GEOCODING_MOCK_2),
            content_type="application/json"
        )
        s1 = SpotFactory(
            name='test',
            location=Point(longitude_1, latitude_1)
        )
        s1.save()
        street_before = s1.address_street
        self.assertEqual(street_before, 'Kolejowa')

        latitude_2, longitude_2 = 52.27904, 20.980366
        url2 = REVERSE_GEOCODING_URL.format(
            latitude=latitude_2,
            longitude=longitude_2,
            api_key=settings.GOOGLE_MAP_API_KEY
        )
        responses.add(
            responses.GET,
            url2,
            body=json.dumps(RESPONSE_GEOCODING_MOCK),
            content_type="application/json"
        )

        import requests; requests.get(url2)  # this sucks but due too https://github.com/getsentry/responses/issues/203

        s1.location.coords = (longitude_2, latitude_2)
        s1.save()
        s1 = Spot.objects.get(pk=s1.pk)
        self.assertEqual(s1.address_street, 'Mickiewicza')

    @responses.activate
    def test_slug_is_updated_correctly_when_location_changes(self):
        latitude_1, longitude_1 = 52.226297, 20.982749
        url = REVERSE_GEOCODING_URL.format(
            latitude=latitude_1,
            longitude=longitude_1,
            api_key=settings.GOOGLE_MAP_API_KEY
        )
        responses.add(
            responses.GET,
            url,
            body=json.dumps(RESPONSE_GEOCODING_MOCK_2),
            content_type="application/json"
        )
        s1 = SpotFactory(
            name='test',
            location=Point(longitude_1, latitude_1)
        )
        s1.save()
        street_before = s1.address_street
        self.assertEqual(
            s1.spot_slug, '{name}-{type}-{city}-{street}-{number}'.format(
                name=s1.name.lower(),
                type=s1.get_spot_type_display().lower(),
                city=s1.address_city.lower(),
                street='kolejowa',
                number=47
            )
        )

        latitude_2, longitude_2 = 52.27904, 20.980366
        url2 = REVERSE_GEOCODING_URL.format(
            latitude=latitude_2,
            longitude=longitude_2,
            api_key=settings.GOOGLE_MAP_API_KEY
        )
        responses.add(
            responses.GET,
            url2,
            body=json.dumps(RESPONSE_GEOCODING_MOCK),
            content_type="application/json"
        )

        import requests; requests.get(url2)  # this sucks but due too https://github.com/getsentry/responses/issues/203

        s1.location.coords = (longitude_2, latitude_2)
        s1.save()
        s1 = Spot.objects.get(pk=s1.pk)
        self.assertEqual(
            s1.spot_slug, '{name}-{type}-{city}-{street}-{number}'.format(
                name=s1.name.lower(),
                type=s1.get_spot_type_display().lower(),
                city=s1.address_city.lower(),
                street='mickiewicza',
                number=74
            )
        )
