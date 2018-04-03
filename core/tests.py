from django.test import TestCase

from accounts.factories import UserFactory
from core.factories.ratings import RatingFactory
from core.factories.spots import SpotFactory
from core.models.ratings import Rating
from core.models.spots import Spot
from utils.factories import TagFactory


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