# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from factory.fuzzy import FuzzyChoice

from accounts.factories import UserFactory
from core.factories.ratings import RatingFactory
from core.models.ratings import Rating
from core.models.spots import Spot
from core.management.commands.create_andi import create_andi


class Command(BaseCommand):

    def handle(self, *args, **options):
        andi = create_andi()
        u2 = UserFactory(email='dummy_user@example.com', mail_verified=True)
        u2.save()
        for spot in Spot.objects.all():
            RatingFactory(
                is_enabled=FuzzyChoice([True, True, True, False]),
                user=andi,
                spot=spot,
                friendly_rate=FuzzyChoice(choice[0] for choice in Rating._meta.get_field('friendly_rate').choices[3:])
            )
            RatingFactory(
                is_enabled=FuzzyChoice([True, False, False, False]),
                user=u2,
                spot=spot,
                friendly_rate=FuzzyChoice(choice[0] for choice in Rating._meta.get_field('friendly_rate').choices[0:3])
            )
