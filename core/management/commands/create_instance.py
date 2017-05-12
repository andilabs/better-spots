# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.conf import settings

from core.models import Instance


class Command(BaseCommand):

    def handle(self, *args, **options):
        Instance.objects.get_or_create(
            name=settings.SPOT_PROJECT_NAME,
            slogan=settings.SPOT_PROJECT_SLOGAN,
            subject=settings.SPOT_PROJECT_SUBJECT,
            main_color=settings.SPOT_PROJECT_MAIN_COLOR,
            description=settings.SPOT_PROJECT_DESCRIPTION,
            bloger_photo=settings.SPOT_PROJECT_BLOGGER_PHOTO,
            instagram=settings.SPOT_PROJECT_INSTAGRAM_URL
        )
