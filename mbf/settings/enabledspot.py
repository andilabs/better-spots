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

SPOT_PROJECT_DESCRIPTION = 'find the disabled people accessible cafes, restaurants and more'

SPOT_PROJECT_SUBJECT = 'Disabled People'

SPOT_PROJECT_MAIN_COLOR = '#4f5fa7'

ENABLED_TOILET_CODE = "toilet_enabled"
ENABLED_TOILET_VERBOSE = "enabled toilet"

ENABLED_ENTRANCE_CODE = "entrance_enabled"
ENABLED_ENTRANCE_VERBOSE = "enabled entrance"

ENABLED_TABLES_CODE = "tables_enabled"
ENABLED_TABLES_VERBOSE = "enabled tables"

FACILITIES_CODE_VERBOSE_MAP = {
    ENABLED_TOILET_CODE: ENABLED_TOILET_VERBOSE,
    ENABLED_ENTRANCE_CODE: ENABLED_ENTRANCE_VERBOSE,
    ENABLED_TABLES_CODE: ENABLED_TABLES_VERBOSE,
}

HSTORE_SCHEMA = [
    {
        "name": ENABLED_TOILET_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": ENABLED_TOILET_VERBOSE
        }
    },
    {
        "name": ENABLED_ENTRANCE_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": ENABLED_ENTRANCE_VERBOSE
        }
    },
    {
        "name": ENABLED_TABLES_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": ENABLED_TABLES_VERBOSE
        }
    }
]
