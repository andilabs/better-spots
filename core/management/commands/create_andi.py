# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from accounts.models import SpotUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        andi = SpotUser.objects.create_superuser(
            email='andi@andilabs.com',
            password='d00r00tk@',
        )
        andi.save()
