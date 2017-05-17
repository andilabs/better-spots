# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from core.models.spots import Spot


class Command(BaseCommand):

    def handle(self, *args, **options):
        for spot in Spot.objects.all():
            spot.save()
