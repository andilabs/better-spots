#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from .common import *

from unipath import Path

DEBUG = True
TEMPLATE_DEBUG = True

INSTANCE_DOMAIN = "127.0.0.1:4000"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'localhost.debug@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

POSTGIS_VERSION = (2, 1, 3)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mbf',
        'USER': 'mbf',
        'HOST': 'localhost',
        'PORT': '5432',
        'PASSWORD': '1234',
    }
}

PROJECT_ROOT_PATH = Path(__file__).ancestor(3)

STATICFILES_DIRS = (
    PROJECT_ROOT_PATH.child('static_assets'),
)


MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/Users/andi/pseudo_static_server_spots/'
MEDIA_ROOT = '/Users/andi/pseudo_media_server_spots/'

TEMPLATE_DIRS = (
     os.path.join(PROJECT_ROOT_PATH, 'templates/'),
)

# SPOT_PROJECT_NAME = 'veganspot'
# SPOT_PROJECT_SLOGAN = 'And, all the world is green!'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing vegans and vegetarians friendly spots'
# SPOT_PROJECT_SUBJECT = 'Vege'
# SPOT_PROJECT_MAIN_COLOR = '#59b84d'

# HSTORE_SCHEMA = [
#   {
#       "name": "vegetarian_menu",
#       "class": "NullBooleanField",
#       "kwargs": {
#           "default": None,
#           "verbose_name": "vegetarian menu"
#       }
#   },
#   {
#       "name": "vegan_menu",
#       "class": "NullBooleanField",
#       "kwargs": {
#           "default": None,
#           "verbose_name": "vegan menu"
#       }
#   }
# ]

# SPOT_PROJECT_NAME = 'enabledspot'
# SPOT_PROJECT_SLOGAN = 'The Brave New Enabled World!'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing the disabled people friendly spots'
# SPOT_PROJECT_SUBJECT = 'Disabled'
# SPOT_PROJECT_MAIN_COLOR = '#4f5fa7'

# HSTORE_SCHEMA = [
#     {
#         "name": "toilet_enabled",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "enabled toilet"
#         }
#     },
#     {
#         "name": "entrance_enabled",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "enabled entrance"
#         }
#     },
#     {
#         "name": "tables_enabled",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "enabled tables"
#         }
#     }
# ]

# SPOT_PROJECT_NAME = 'momspot'
# SPOT_PROJECT_SLOGAN = 'Mom\'s Revolution starts in cafes!'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing moms and children friendly spots'
# SPOT_PROJECT_SUBJECT = 'Moms'
# SPOT_PROJECT_MAIN_COLOR = '#eb386f'

# HSTORE_SCHEMA = [
#   {
#       "name": "baby_changing",
#       "class": "NullBooleanField",
#       "kwargs": {
#           "default": None,
#           "verbose_name": "baby changing facilites"
#       }
#   },
#   {
#       "name": "playroom",
#       "class": "NullBooleanField",
#       "kwargs": {
#           "default": None,
#           "verbose_name": "playroom for kids"
#       }
#   },
#   {
#       "name": "kids_menu",
#       "class": "NullBooleanField",
#       "kwargs": {
#           "default": None,
#           "verbose_name": "kids menu"
#       }
#   }
# ]

SPOT_PROJECT_NAME = 'dogspot'
SPOT_PROJECT_SLOGAN = 'Wow the World!'
SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing dog friendly spots'
SPOT_PROJECT_SUBJECT = 'Dog'
SPOT_PROJECT_MAIN_COLOR = '#fcbd41'


FRESH_WATER_CODE = "fresh_water"
FRESH_WATER_VERBOSE = "fresh water served"

SNACKS_CODE = "snacks"
SNCACKS_VERBOSE = "dog snakcs"

SPECIAL_MENU_CODE = "dedicated_dogs_menu"
SPECIAL_MENU_VERBOSE = "special menu for dogs"

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


SPOT_PROJECT_FAVICON_URL = os.path.join(
    'static',
    SPOT_PROJECT_NAME,
    'favicon.ico'
)

SPOT_PROJECT_BLOGERS = os.path.join(STATIC_URL, SPOT_PROJECT_NAME, 'bloger_photo.jpg')

MIDDLEWARE_CLASSES = ('utils.performance.db_queries.QueryCountDebugMiddleware',) + MIDDLEWARE_CLASSES

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG', # message level to be written to console
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        'django.db': {
            # django also has database level logging
        },
    },
}

SPOT_FACILITIES = [d['name'] for d in HSTORE_SCHEMA]

SPOT_FACILITIES_VERBOSE_NAMES = [(d['kwargs']['verbose_name'],d['name']) for d in HSTORE_SCHEMA]
