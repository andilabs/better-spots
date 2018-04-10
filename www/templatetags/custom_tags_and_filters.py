import os
import urllib.parse as urlparse

from django import template
from django.conf import settings
from django.contrib.messages import constants as DEFAULT_MESSAGE_LEVELS

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


@register.filter
def bootstrap_message_classes(message):
    """
    Return the message classes for a message
    # copied from https://github.com/dyve/django-bootstrap3/blob/master/bootstrap3/templatetags/bootstrap3.py
    # didn't want to couple with django-bootstrap3 to tight, just nice django messages styling wanted
    """
    MESSAGE_LEVEL_CLASSES = {
        DEFAULT_MESSAGE_LEVELS.DEBUG: "alert alert-warning",
        DEFAULT_MESSAGE_LEVELS.INFO: "alert alert-info",
        DEFAULT_MESSAGE_LEVELS.SUCCESS: "alert alert-success",
        DEFAULT_MESSAGE_LEVELS.WARNING: "alert alert-warning",
        DEFAULT_MESSAGE_LEVELS.ERROR: "alert alert-danger",
    }

    extra_tags = None
    try:
        extra_tags = message.extra_tags
    except AttributeError:
        pass
    if not extra_tags:
        extra_tags = ""
    classes = [extra_tags]
    try:
        level = message.level
    except AttributeError:
        pass
    else:
        try:
            classes.append(MESSAGE_LEVEL_CLASSES[level])
        except KeyError:
            classes.append("alert alert-danger")
    return ' '.join(classes).strip()
