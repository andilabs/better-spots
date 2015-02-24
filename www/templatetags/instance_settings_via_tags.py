from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    return str(getattr(settings, name, ""))
