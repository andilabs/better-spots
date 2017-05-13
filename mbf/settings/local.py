#!/usr/bin/python
# -*- coding: utf-8 -*-

from .common import *

from unipath import Path

from mbf.settings.instance_configs.dogspot import *
SPOT_PROJECT_NAME = 'dogspot'
#
# from mbf.settings.instance_configs.momspot import *
# SPOT_PROJECT_NAME = 'momspot'
#
# from mbf.settings.instance_configs.enabledspot import *
# SPOT_PROJECT_NAME = 'enabledspot'
#
# from mbf.settings.instance_configs.veganspot import *
# SPOT_PROJECT_NAME = 'veganspot'


DEBUG = True

INSTANCE_DOMAIN = "192.168.33.13:8000"

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
STATIC_ROOT = '/pseudo_static_server_spots/'

# TEMPLATE_DIRS = (
#      os.path.join(PROJECT_ROOT_PATH, 'templates/'),
# )


SPOT_FACILITIES = [d['name'] for d in HSTORE_SCHEMA]

SPOT_FACILITIES_VERBOSE_NAMES = [(d['kwargs']['verbose_name'],d['name']) for d in HSTORE_SCHEMA]

INTERNAL_IPS = ('192.168.33.1', )
