# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from core.factories.ratings import RatingFactory
from core.models.spots import Spot
from core.management.commands.create_andi import create_andi


class Command(BaseCommand):

    def handle(self, *args, **options):
        andi = create_andi()
        for spot in Spot.objects.all():
            RatingFactory(
                is_enabled=True,
                friendly_rate=4,
                user=andi,
                spot=spot
            )
