from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from accounts.factories import UserFactory, UserFavouritesSpotListFactory
from accounts.models import UserFavouritesSpotList
from core.factories.spots import SpotFactory


class UserFavouritesAPITestCase(APITestCase):

    def setUp(self):
        self.s1 = SpotFactory()
        self.s2 = SpotFactory()
        self.s3 = SpotFactory()

    def test_add_spot_to_user_favourites_when_non_existing_user(self):
        url = reverse('api:user-favourites-list', kwargs={'user_pk': 666})
        response = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_spot_user_favourites_when_not_authenticated(self):
        user = UserFactory(email='a@b.pl')
        url = reverse('api:user-favourites-list', kwargs={'user_pk': user.pk})
        response = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_spot_to_another_users_favourites_is_not_allowed(self):
        u1 = UserFactory(email='potential@victim.com')
        u2 = UserFactory(email='crazy@hacker.com')
        u2.set_password('blah')
        u2.save()

        self.client.login(email=u2.email, password='blah')
        url = reverse('api:user-favourites-list', kwargs={'user_pk': u1.pk})
        response = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_spot_to_user_favourites(self):
        user = UserFactory(email='a@b.pl')
        user.set_password('blah')
        user.save()

        self.client.login(email=user.email, password='blah')
        url = reverse('api:user-favourites-list', kwargs={'user_pk': user.pk})
        response = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.favourites.count(), 1)

    def test_adding_spot_already_existing_in_user_favourites(self):
        user = UserFactory(email='a@b.pl')
        user.set_password('blah')
        user.save()

        self.client.login(email=user.email, password='blah')
        url = reverse('api:user-favourites-list', kwargs={'user_pk': user.pk})
        _ = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(user.favourites.count(), 1)
        response = self.client.post(url, {
            'spot': "{}".format(self.s1.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            response.json(),
            {'non_field_errors': ['Already in user favourites']}
        )
        self.assertEqual(user.favourites.count(), 1)

    def test_removing_another_user_favourite_spot_not_allowed(self):
        u1 = UserFactory(email='potential@victim.com')
        UserFavouritesSpotListFactory(
            user=u1,
            spot=self.s1
        )
        UserFavouritesSpotListFactory(
            user=u1,
            spot=self.s2
        )

        u2 = UserFactory(email='crazy@hacker.com')
        u2.set_password('blah')
        u2.save()

        self.client.login(email=u2.email, password='blah')
        url = reverse('api:user-favourites-detail', kwargs={
            'user_pk': u1.pk,
            'pk': UserFavouritesSpotList.objects.filter(user=u1).first().pk
        })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_updating_another_user_favourite_spot_not_allowed(self):
        u1 = UserFactory(email='potential@victim.com')
        u2 = UserFactory(email='crazy@hacker.com')
        u2.set_password('blah')
        u2.save()

        uf1 = UserFavouritesSpotListFactory(
            user=u1,
            spot=self.s1
        )

        self.client.login(email=u2.email, password='blah')
        url = reverse('api:user-favourites-detail', kwargs={
            'user_pk': u1.pk,
            'pk': uf1.pk
        })
        response = self.client.patch(url, {
            'spot': "{}".format(self.s3.pk)
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(uf1.spot.pk, self.s1.pk)

    def test_successful_remove_from_favourites(self):
        user = UserFactory(email='a@b.pl')
        user.set_password('blah')
        user.save()

        uf1 = UserFavouritesSpotListFactory(
            user=user,
            spot=self.s1
        )
        uf2 = UserFavouritesSpotListFactory(
            user=user,
            spot=self.s2
        )

        self.client.login(email=user.email, password='blah')
        url = reverse('api:user-favourites-detail', kwargs={
            'user_pk': user.pk,
            'pk': uf1.pk
        })
        self.assertEqual(user.favourites.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(user.favourites.count(), 1)
        url = reverse('api:user-favourites-detail', kwargs={
            'user_pk': user.pk,
            'pk': uf2.pk
        })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(user.favourites.count(), 0)

    def test_get_user_favourites(self):
        u1 = UserFactory(email='a@b.pl')
        u2 = UserFactory(email='c@d.pl')
        _ = UserFavouritesSpotListFactory(
            user=u1,
            spot=self.s1
        )
        _ = UserFavouritesSpotListFactory(
            user=u1,
            spot=self.s2
        )
        _ = UserFavouritesSpotListFactory(
            user=u2,
            spot=self.s3
        )
        url1 = reverse('api:user-favourites-list', kwargs={'user_pk': u1.pk})
        response1 = self.client.get(url1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.json()['results']), 2)

        url2 = reverse('api:user-favourites-list', kwargs={'user_pk': u2.pk})
        response2 = self.client.get(url2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.json()['results']), 1)
