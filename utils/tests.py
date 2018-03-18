import json
import responses

from django.conf import settings
from django.test import TestCase

from utils.geocoding import reverse_geocoding, REVERSE_GEOCODING_URL
from utils.text import get_unaccented

RESPONSE_GEOCODING_MOCK = {
    'results': [
        {
            'address_components': [
                {'long_name': '74', 'short_name': '74', 'types': ['street_number']},
                {'long_name': 'Mickiewicza', 'short_name': 'Mickiewicza', 'types': ['route']},
                {'long_name': 'Żoliborz', 'short_name': 'Żoliborz', 'types': ['political', 'sublocality', 'sublocality_level_1']},
                {'long_name': 'Warszawa', 'short_name': 'Warszawa', 'types': ['locality', 'political']},
                {'long_name': 'Warszawa', 'short_name': 'Warszawa', 'types': ['administrative_area_level_2', 'political']},
                {'long_name': 'mazowieckie', 'short_name': 'mazowieckie', 'types': ['administrative_area_level_1', 'political']},
                {'long_name': 'Poland', 'short_name': 'PL', 'types': ['country', 'political']}
            ],
            'formatted_address': 'Mickiewicza 74, Warszawa, Poland',
            'geometry': {'location': {'lat': 52.2790223, 'lng': 20.980648},
                         'location_type': 'ROOFTOP',
                         'viewport': {'northeast': {'lat': 52.2803712802915, 'lng': 20.9819969802915},
                                      'southwest': {'lat': 52.2776733197085, 'lng': 20.9792990197085}}
                         },
            'place_id': 'ChIJxXoMrOfLHkcRBAFsrjKGcMc',
            'types': ['street_address']
        }
    ],
    'status': 'OK'
}


class TestGoogleAPIGeocodingConsumer(TestCase):

    @responses.activate
    def test_geocoding(self):
        latitude, longitude = 52.27904, 20.980366
        responses.add(
            responses.GET,
            REVERSE_GEOCODING_URL.format(
                latitude=latitude,
                longitude=longitude,
                api_key=settings.GOOGLE_API_KEY
            ),
            body=json.dumps(RESPONSE_GEOCODING_MOCK),
            content_type="application/json")

        response = reverse_geocoding(latitude, longitude)
        self.assertEqual(response, {'address_city': 'Warszawa',
                                    'address_country': 'Poland',
                                    'address_number': '74',
                                    'address_street': 'Mickiewicza'})


class TestUnaccent(TestCase):

    PL_CHARS = u"ą, ć, ę, ł, ń, ó, ś, ź, ż".split(', ')

    def test_basic_polish_charters_escaping(self):
        correct_unnacent = 'a, c, e, l, n, o, s, z, z'.split(', ')
        for index, pl_char in enumerate(self.PL_CHARS):
            self.assertEqual(get_unaccented(pl_char), correct_unnacent[index])
            self.assertEqual(get_unaccented(pl_char.upper()), correct_unnacent[index].upper())
