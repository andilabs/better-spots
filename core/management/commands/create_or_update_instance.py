from django.conf import settings
from django.core.management.base import BaseCommand

from core.models.instance import Instance


def create_or_update_instance():

    Instance.objects.update_or_create(
        pk=1,
        defaults={
            'name': settings.SPOT_PROJECT_NAME,
            'slogan': settings.SPOT_PROJECT_SLOGAN,
            'subject': settings.SPOT_PROJECT_SUBJECT,
            'main_color': settings.SPOT_PROJECT_MAIN_COLOR,
            'description': settings.SPOT_PROJECT_DESCRIPTION,
            'instagram': settings.SPOT_PROJECT_INSTAGRAM_USERNAME,
            'blogger_photo': settings.SPOT_PROJECT_BLOGGER_PHOTO,
        }
    )


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_or_update_instance()
