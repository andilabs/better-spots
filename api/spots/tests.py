from django.contrib.gis.geos import Point
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from api.spots.serializers import SpotSerializer
from core.factories.spots import SpotFactory
from utils.factories import TagFactory
from utils.geodistance import get_distance_between_points


class ApiSpotsTest(APITestCase):

    def test_api_list_spots(self):
        """
        Ensure all spots were returned
        """
        [SpotFactory() for _ in range(5)]
        url = reverse('api:spot-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 5)

    def test_filtering_by_tags(self):
        tag_xxx = TagFactory(text='xxx')
        tag_yyy = TagFactory(text='yyy')
        s1 = SpotFactory()
        s2 = SpotFactory()
        s3 = SpotFactory()
        s1.tags.add(tag_xxx)
        s2.tags.add(tag_yyy)
        s3.tags.add(*[tag_xxx, tag_yyy])

        tested_tag_xxx = 'xxx'
        url = '{}?tags={}'.format(reverse('api:spot-list'), tested_tag_xxx)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertIn(tested_tag_xxx, result['tags'])

        tested_tag_yyy = 'yyy'
        url = '{}?tags={}'.format(reverse('api:spot-list'), tested_tag_yyy)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertIn(tested_tag_yyy, result['tags'])

        url = '{}?tags={}&tags={}'.format(reverse('api:spot-list'), tested_tag_yyy, tested_tag_xxx)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertTrue(
                tested_tag_yyy in result['tags'] or tested_tag_xxx in result['tags']
            )


class ApiSpotsByDistanceFilteringTest(APITestCase):

    def setUp(self):
        self.user_location = {'lat': 52.2302004, 'lon': 21.0125331}

        self.spot_1 = SpotFactory(location=Point(21.0066200000000016, 52.2317699999999974), name='Kulturalna')
        self.spot_2 = SpotFactory(location=Point(21.0164000000000009, 52.2214499999999973), name='Szwejk')
        self.spot_3 = SpotFactory(location=Point(21.0227600000000017, 52.2395899999999997), name='Kafka')

    @staticmethod
    def get_url_with_location_and_radius(lat, lon, desired_radius):
        return "{resource_uri}?location_0={lat}&location_1={lon}&location_2={desired_radius}".format(
            resource_uri=reverse('api:spot-list'),
            lat=lat,
            lon=lon,
            desired_radius=desired_radius
        )

    def get_dict_extended_by_distance(self, dict):
        distance = get_distance_between_points(
            point_a=(dict['location']['latitude'], dict['location']['longitude']),
            point_b=(self.user_location['lat'], self.user_location['lon'])
        )
        dict.update({'distance': distance})
        return dict

    def test_filtering_within_radius_from_given_location_when_nothing(self):
        url = self.get_url_with_location_and_radius(
            lat=self.user_location['lat'],
            lon=self.user_location['lon'],
            desired_radius=50
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 0)

    def test_filtering_within_radius_from_given_location_500m(self):

        url = self.get_url_with_location_and_radius(
            lat=self.user_location['lat'],
            lon=self.user_location['lon'],
            desired_radius=500
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'], self.spot_1.name)

    def test_filtering_within_radius_from_given_location_1100m(self):

        url = self.get_url_with_location_and_radius(
            lat=self.user_location['lat'],
            lon=self.user_location['lon'],
            desired_radius=1100
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)
        self.assertListEqual(response.json()['results'],
                             [self.get_dict_extended_by_distance(SpotSerializer(self.spot_1).data),
                              self.get_dict_extended_by_distance(SpotSerializer(self.spot_2).data)])

    def test_filtering_within_radius_from_given_location_1500m(self):
        url = self.get_url_with_location_and_radius(
            lat=self.user_location['lat'],
            lon=self.user_location['lon'],
            desired_radius=1500
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 3)
        self.assertListEqual(response.json()['results'],
                             [self.get_dict_extended_by_distance(SpotSerializer(self.spot_1).data),
                              self.get_dict_extended_by_distance(SpotSerializer(self.spot_2).data),
                              self.get_dict_extended_by_distance(SpotSerializer(self.spot_3).data)])
