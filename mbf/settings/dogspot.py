#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "dogspot.eu"

EMAIL_HOST_USER = 'no-reply@dogspot.eu'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25


STATIC_ROOT = '/home/ubuntu/dogspot.eu/static_assets/'
MEDIA_ROOT = '/home/ubuntu/dogspot.eu/media_assets/'

POSTGIS_VERSION = (2, 1, 2)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dogspot',
        'USER': 'dogspot',
        'PASSWORD': 'c9c38a6dc8cdb66a0c416a9e1f8eac21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

RAVEN_CONFIG = {
    'dsn': 'https://4fa3854da7cd48f1a8b7a14a349d251d:c9cd00443c434d5fb1b204d8e5a95ffa@app.getsentry.com/29551',
}

SPOT_PROJECT_NAME = 'dogspot'
GRAPPELLI_ADMIN_TITLE = SPOT_PROJECT_NAME.capitalize()

SPOT_PROJECT_SLOGAN = 'Wow the World!'

SPOT_PROJECT_DESCRIPTION = 'find dog friendly cafes, restaurants and more'

SPOT_PROJECT_SUBJECT = 'Dog'

SPOT_PROJECT_MAIN_COLOR = '#fcbd41'

FRESH_WATER_CODE = "fresh_water"
FRESH_WATER_VERBOSE = "fresh water served"

SNACKS_CODE = "dog_snacks"
SNCACKS_VERBOSE = "dog treats"

SPECIAL_MENU_CODE = "dedicated_dogs_menu"
SPECIAL_MENU_VERBOSE = "special menu for dogs"

SPOT_PROJECT_INSTAGRAM_URL = "https://www.instagram.com/dogspoteu/"

FACILITIES_CODE_VERBOSE_MAP = {
    FRESH_WATER_CODE: FRESH_WATER_VERBOSE,
    SNACKS_CODE: SNCACKS_VERBOSE,
    SPECIAL_MENU_CODE: SPECIAL_MENU_VERBOSE
}

HSTORE_SCHEMA = [
    {
        "name": FRESH_WATER_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": FRESH_WATER_VERBOSE
        }
    },
    {
        "name": SNACKS_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": SNCACKS_VERBOSE
        }
    },
    {
        "name": SPECIAL_MENU_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": SPECIAL_MENU_VERBOSE
        }
    }
]


