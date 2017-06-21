# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from accounts.factories import UserFactory
from core.factories.ratings import RatingFactory
from core.models.spots import Spot
from core.management.commands.create_andi import create_andi


class Command(BaseCommand):

    def handle(self, *args, **options):
        andi = create_andi()
        u2 = UserFactory(email='dummy_user@example.com', mail_verified=True)
        u2.save()
        for spot in Spot.objects.all():
            RatingFactory(
                is_enabled=True,
                user=andi,
                spot=spot
            )
            RatingFactory(
                is_enabled=False,
                user=u2,
                spot=spot
            )
