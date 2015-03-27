from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    return str(getattr(settings, name, ""))


@register.filter
def keyvalue(dict, key):
    return dict.get(key)


@register.filter
def get_verbose_name(self):
    return self._meta.verbose_name
