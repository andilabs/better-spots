# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from accounts.models import SpotUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not SpotUser.objects.filter(email='andi@andilabs.com').exists():
            andi = SpotUser.objects.create_superuser(
                email='andi@andilabs.com',
                password='123qwe',
            )
            andi.save()
