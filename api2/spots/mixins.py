from django.shortcuts import get_object_or_404

from core.models.spots import Spot


class ObjectInSpotContextMixin(object):

    def validate(self, attrs):
        attrs['spot'] = get_object_or_404(Spot, pk=self.context['view'].kwargs['spot_pk'])
        return attrs
