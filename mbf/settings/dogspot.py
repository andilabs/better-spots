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

SPOT_PROJECT_SLOGAN = 'Wow the World!'

SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing dog friendly spots'

SPOT_PROJECT_SUBJECT = 'Dog'

SPOT_PROJECT_MAIN_COLOR = '#fcbd41'

HSTORE_SCHEMA = [
    {
        "name": "fresh_water",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "fresh water served"
        }
    },
    {
        "name": "dog_snacks",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "snacks"
        }
    },
    {
        "name": "dedicated_dogs_menu",
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": "special menu for dogs"
        }
    }
]
