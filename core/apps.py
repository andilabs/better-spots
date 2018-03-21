from django.apps import AppConfig
from django.db.models.signals import post_save

from core.signals import fill_address_based_on_reverse_geocoding


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        post_save.connect(fill_address_based_on_reverse_geocoding, sender='core.Spot')
