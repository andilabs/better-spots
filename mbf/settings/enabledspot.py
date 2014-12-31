#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "enabledspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@enabledspot.eu'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

STATIC_ROOT = '/home/ubuntu/dogspot.eu/static_assets/'
POSTGIS_VERSION = (2, 1, 2)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'enabledspot',
        'USER': 'enabledspot',
        'PASSWORD': 'c9c38a6dc8cdb66a0c416a9e1f8eac21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SPOT_PROJECT_NAME = 'enabledspot'

SPOT_PROJECT_BRAND_LOGO = ''

SPOT_PROJECT_CERTIFICATE_LOGO = ''

SPOT_PROJECT_SLOGAN = 'Enabled World '

SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing spots in terms of being enabled for people with disabilites'

SPOT_PROJECT_SUBJECT = 'people with disabilites'
