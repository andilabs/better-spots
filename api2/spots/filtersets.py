from django_filters import (
    Filter,
    FilterSet,
    ModelMultipleChoiceFilter,
)
from django import forms

from core.models.spots import Spot
from utils.models import Tag


class LatLonRadiusWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.TextInput, forms.TextInput, forms.TextInput)
        super(LatLonRadiusWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        # if value:
        #     return [value.lat, value.lon, value.radius]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return '-'.join(rendered_widgets)


class LatLonRadiusField(forms.MultiValueField):
    widget = LatLonRadiusWidget

    def __init__(self, fields=None, *args, **kwargs):
        if fields is None:
            fields = (
                forms.DecimalField(label='lat'),
                forms.DecimalField(label='lon'),
                forms.IntegerField(label='radius')
            )
        super(LatLonRadiusField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            # lat, lon, radius = data_list
            # return {'lat': lat, 'lon': lon, 'radius': radius}
            return data_list
        return None

from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr


class LatLonRadiusFilter(Filter):
    field_class = LatLonRadiusField

    def filter(self, qs, value):
        if value:
            value_lat = value[0]
            value_lon = value[1]
            value_radius = value[2]
            if value_lat is not None and value_lon is not None and value_radius is not None:
                lookup = 'location__distance_lte'
                user_location = fromstr("POINT(%s %s)" % (value_lon, value_lat))
                desired_radius = {'m': value_radius}
                return self.get_method(qs)(**{lookup: (user_location, D(**desired_radius))})

                # if value.start is not None:
                #     qs = self.get_method(qs)(**{'%s__gte' % self.name: value.start})
                # if value.stop is not None:
                #     qs = self.get_method(qs)(**{'%s__lte' % self.name: value.stop})
        return qs


class SpotFilterSet(FilterSet):
    location = LatLonRadiusFilter()
    tags = ModelMultipleChoiceFilter(
        name='tags__text',
        queryset=Tag.objects.all(),
        to_field_name='text',
        # conjoined=True, #makes AND - only spots having all the tags will be returned
    )

    class Meta:
        model = Spot
        fields = [
            'name',
            'location',
            'spot_type',
            'tags',
        ]

