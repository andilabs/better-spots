import os
import urllib.parse as urlparse

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    return str(getattr(settings, name, ""))


@register.simple_tag
def settings_value_static(name):
    return os.path.join(settings.STATIC_URL, str(getattr(settings, name, "")))


@register.simple_tag
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()


@register.filter
def keyvalue(dict, key):
    return dict.get(key)


@register.filter
def get_verbose_name(self):
    return self._meta.verbose_name


@register.filter(name='add_css')
def addcss(value, arg):
    if value.field.widget.attrs.get('class'):
        arg = value.field.widget.attrs.get('class') + ' ' + arg
    return value.as_widget(attrs={'class': arg})


@register.simple_tag
def pagination_filters_aware(querystring, page):
    querydict = dict(urlparse.parse_qsl(querystring))
    querydict.update({'page': page})
    return "?{}".format(urlparse.urlencode(querydict))
