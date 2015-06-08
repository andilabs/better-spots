from django.conf import settings

from core.models import Instance


def spot_facilities(request):
    return {'HSTORE_SCHEMA': settings.HSTORE_SCHEMA}


def instance(request):
    instance = Instance.objects.get()
    return {'INSTANCE': instance}
