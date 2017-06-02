# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from accounts.models import User


def create_andi():
    if not User.objects.filter(email='andi@andilabs.com').exists():
        andi = User.objects.create_superuser(
            email='andi@andilabs.com',
            password='123qwe',
        )
        andi.save()
    else:
        andi = User.objects.get(email='andi@andilabs.com')

    return andi


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_andi()
