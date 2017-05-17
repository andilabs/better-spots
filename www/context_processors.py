from django.conf import settings

from core.models.instance import Instance
from core.models.spots import Spot


def spot_facilities(request):
    return {'HSTORE_SCHEMA': settings.HSTORE_SCHEMA}


def instance(request):
    instance = Instance.objects.get()
    all_cities = Spot.objects.order_by().values_list('address_city', flat=True).distinct()
    return {'INSTANCE': instance, 'ALL_CITIES': all_cities, 'SPOT_FACILITIES_VERBOSE_NAMES': settings.SPOT_FACILITIES_VERBOSE_NAMES}
