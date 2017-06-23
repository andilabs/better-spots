from core.models.spots import Spot


class ObjectInSpotContextMixin(object):
    def validate(self, attrs):
        attrs['spot'] = Spot.objects.get(pk=self.context['view'].kwargs['spot_pk'])
        return attrs
