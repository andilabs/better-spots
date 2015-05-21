#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "enabledspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@enabledspot.eu'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

RAVEN_CONFIG = {
    'dsn': 'https://e44acaed8e4c4940a28d46b1b0ad1819:67601b0d9cc34321b6a38b31e1b79e22@app.getsentry.com/37317',
}

STATIC_ROOT = '/home/ubuntu/enabledspot.eu/static_assets/'
MEDIA_ROOT = '/home/ubuntu/enabledpot.eu/media_assets/'

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
GRAPPELLI_ADMIN_TITLE = SPOT_PROJECT_NAME.capitalize()

SPOT_PROJECT_SLOGAN = 'The Brave New Enabled World!'

SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing the disabled people accessible spots'

SPOT_PROJECT_SUBJECT = 'Disabled People'

SPOT_PROJECT_MAIN_COLOR = '#4f5fa7'

HSTORE_SCHEMA = [
    {
        "name": "toilet_enabled",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "enabled toilet"
        }
    },
    {
        "name": "entrance_enabled",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "enabled entrance"
        }
    },
    {
        "name": "tables_enabled",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "enabled tables"
        }
    }
]
