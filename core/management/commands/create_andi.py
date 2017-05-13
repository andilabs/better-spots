# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email='andi@andilabs.com').exists():
            andi = User.objects.create_superuser(
                email='andi@andilabs.com',
                password='123qwe',
            )
            andi.save()
