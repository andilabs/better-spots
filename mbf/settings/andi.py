#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from .common import *

from unipath import Path

DEBUG = True
TEMPLATE_DEBUG = True

INSTANCE_DOMAIN = "127.0.0.1:8000"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'localhost.debug@gmail.com'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

POSTGIS_VERSION = (2, 1, 3)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'andispot',
        'USER': 'andi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

PROJECT_ROOT_PATH = Path(__file__).ancestor(3)

STATICFILES_DIRS = (
    PROJECT_ROOT_PATH.child('static_assets'),
)


MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/Users/andi/pseudo_static_server_spots/'
MEDIA_ROOT = '/Users/andi/pseudo_media_server_spots/'

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

SPOT_PROJECT_NAME = 'momspot'
SPOT_PROJECT_SLOGAN = 'Mom\'s Revolution starts in cafes!'
SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing moms and children friendly spots'
SPOT_PROJECT_SUBJECT = 'Moms'
SPOT_PROJECT_MAIN_COLOR = '#eb386f'

HSTORE_SCHEMA = [
  {
      "name": "baby_changing",
      "class": "NullBooleanField",
      "kwargs": {
          "default": None,
          "verbose_name": "baby changing facilites"
      }
  },
  {
      "name": "playroom",
      "class": "NullBooleanField",
      "kwargs": {
          "default": None,
          "verbose_name": "playroom for kids"
      }
  },
  {
      "name": "kids_menu",
      "class": "NullBooleanField",
      "kwargs": {
          "default": None,
          "verbose_name": "kids menu"
      }
  }
]

# SPOT_PROJECT_NAME = 'dogspot'
# SPOT_PROJECT_SLOGAN = 'Wow the World!'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing dog friendly spots'
# SPOT_PROJECT_SUBJECT = 'Dog'
# SPOT_PROJECT_MAIN_COLOR = '#fcbd41'

# HSTORE_SCHEMA = [
#     {
#         "name": "fresh_water",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "fresh water served"
#         }
#     },
#     {
#         "name": "dedicated_dogs_menusnacks",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "snacks"
#         }
#     },
#     {
#         "name": "dedicated_dogs_menu",
#         "class": "NullBooleanField",
#         "kwargs": {
#             "default": None,
#             "verbose_name": "special menu for dogs"
#         }
#     }
# ]

SPOT_PROJECT_FAVICON_URL = os.path.join('static', SPOT_PROJECT_NAME, 'favicon.ico')
