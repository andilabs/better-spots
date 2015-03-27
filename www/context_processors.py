from django.conf import settings


def spot_facilities(request):
    return {'HSTORE_SCHEMA': settings.HSTORE_SCHEMA}
