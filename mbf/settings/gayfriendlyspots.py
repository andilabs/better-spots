#!/usr/bin/python
# -*- coding: utf-8 -*-

from .production import *


INSTANCE_DOMAIN = "gayfriendlyspots.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@gayfriendlyspots.com'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gayfriendlyspots',
        'USER': 'gayfriendlyspots',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}