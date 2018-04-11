from django import forms
from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models.functions import Distance as DistanceFun
from django.contrib.gis.geos import fromstr

from django_filters import rest_framework as filters, CharFilter

from core.models.spots import Spot
from utils.models import Tag
from utils.search import spots_full_text_search


class LatLonRadiusWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (forms.widgets.NumberInput(attrs={'name': 'dupa', 'step': 0.000001}),
                    forms.widgets.NumberInput(attrs={'step': 0.000001}),
                    forms.widgets.NumberInput)
        super(LatLonRadiusWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.lat, value.lon, value.radius]
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
        return data_list


class LatLonRadiusFilter(filters.Filter):
    field_class = LatLonRadiusField

    def filter(self, qs, value):
        if value:
            value_lat = value[0]
            value_lon = value[1]
            value_radius_in_meters = value[2]
            if value_lat and value_lon and value_radius_in_meters:
                user_location = fromstr(
                    "POINT({value_lon} {value_lat})".format(value_lon=value_lon, value_lat=value_lat)
                )
                return qs.filter(
                    location__distance_lte=(user_location, Distance(m=value_radius_in_meters))
                ).annotate(distance=DistanceFun('location', user_location)).order_by('distance')

        return qs


class SpotFilterSet(filters.FilterSet):
    location = LatLonRadiusFilter()
    tags = filters.ModelMultipleChoiceFilter(
        'tags__text',
        queryset=Tag.objects.all(),
        to_field_name='text',
        # conjoined=True, #makes AND - only spots having all the tags will be returned
    )
    address_city = filters.CharFilter(lookup_expr='unaccent', required=False)

    class Meta:
        model = Spot
        fields = [
            'is_certificated',
            'name',
            'location',
            'spot_type',
            'tags',
        ]


class SpotFullTextSearchFilterSet(filters.FilterSet):
    search_query = CharFilter(method='my_custom_filter')

    class Meta:
        model = Spot
        fields = []

    @property
    def qs(self):
        return spots_full_text_search(self.data.get('search_query'))
