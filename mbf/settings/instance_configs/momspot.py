#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "momspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@momspot.eu'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

RAVEN_CONFIG = {
    'dsn': 'https://c2ed6b81264746a0b97644c7fedd29d4:f75054def0234501b24baf4c512e8613@app.getsentry.com/37316',
}

STATIC_ROOT = '/home/ubuntu/momspot.eu/static_assets/'
MEDIA_ROOT = '/home/ubuntu/momspot.eu/media_assets/'

POSTGIS_VERSION = (2, 1, 2)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'momspot',
        'USER': 'momspot',
        'PASSWORD': 'c9c38a6dc8cdb66a0c416a9e1f8eac21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SPOT_PROJECT_NAME = 'momspot'
GRAPPELLI_ADMIN_TITLE = SPOT_PROJECT_NAME.capitalize()


SPOT_PROJECT_SLOGAN = 'Mom\'s Revolution starts in cafes!'

SPOT_PROJECT_DESCRIPTION = 'find moms and children friendly cafes, restaurants and more'

SPOT_PROJECT_SUBJECT = 'Mom'

SPOT_PROJECT_MAIN_COLOR = '#eb386f'

BABY_CHANGING_CODE = "baby_changing"
BABY_CHANGING_VERBOSE = "baby changing facilites"

PLAYROOM_CODE = "playroom"
PLAYROOM_VERBOSE = "playroom for kids"

KIDS_MENU_CODE = "kids_menu"
KIDS_MENU_VERBOSE = "kids menu"

SPOT_PROJECT_INSTAGRAM_URL = "https://www.instagram.com/momspoteu/"


FACILITIES_CODE_VERBOSE_MAP = {
    BABY_CHANGING_CODE: BABY_CHANGING_VERBOSE,
    PLAYROOM_CODE: PLAYROOM_VERBOSE,
    KIDS_MENU_CODE: KIDS_MENU_VERBOSE,
}

HSTORE_SCHEMA = [
    {
        "name": BABY_CHANGING_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": BABY_CHANGING_VERBOSE
        }
    },
    {
        "name": PLAYROOM_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": PLAYROOM_VERBOSE
        }
    },
    {
        "name": KIDS_MENU_CODE,
        "class": "NullBooleanField",
        "kwargs": {
            "default": None,
            "verbose_name": KIDS_MENU_VERBOSE
        }
    }
]
