#!/usr/bin/python
# -*- coding: utf-8 -*-

from .common import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTANCE_DOMAIN = "127.0.0.1:8000"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'localhost.debug@gmail.com'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dogspot',
        'USER': 'dogspot',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/Users/andi/dogspot_pseudo_static_media_server/'

SPOT_PROJECT_NAME = 'gayfriendlyspots'

SPOT_PROJECT_BRAND_LOGO = ''

SPOT_PROJECT_CERTIFICATE_LOGO = ''

SPOT_PROJECT_SLOGAN = 'Let\'s make the difference by diversity!'

SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing LGBT friendly spots'

SPOT_PROJECT_SUBJECT = 'gay'
