from core.models.instance import Instance
from core.models.spots import Spot


def instance(request):
    instance = Instance.objects.get()
    all_cities = Spot.objects.order_by().values_list('address_city', flat=True).distinct()
    return {'INSTANCE': instance, 'ALL_CITIES': all_cities}
