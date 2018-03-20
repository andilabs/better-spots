from django.conf import settings
from django.core.management.base import BaseCommand

from utils.models import Tag


def create_tags():
    for tag_pk, tag_name in settings.TAGS.items():
        Tag.objects.update_or_create(
            pk=tag_pk,
            defaults={'pk': tag_pk, 'text': tag_name}
        )


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_tags()
