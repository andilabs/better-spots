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

SPOT_PROJECT_NAME = 'veganspot'
SPOT_PROJECT_SLOGAN = 'And, all the world is green!'
SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing vegans and vegetarians friendly spots'
SPOT_PROJECT_SUBJECT = 'Vege'


# SPOT_PROJECT_NAME = 'enabledspot'
# SPOT_PROJECT_SLOGAN = 'The Brave New Enabled World '
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing spots in terms of being enabled for people with disabilites'
# SPOT_PROJECT_SUBJECT = 'Disabled'

# SPOT_PROJECT_NAME = 'momspot'
# SPOT_PROJECT_SLOGAN = 'Moms\' Revolution starts in cafes!'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing moms and childrens friendly spots'
# SPOT_PROJECT_SUBJECT = 'Moms'

# SPOT_PROJECT_NAME = 'dogspot'
# SPOT_PROJECT_SLOGAN = 'Wow the World !'
# SPOT_PROJECT_DESCRIPTION = 'Is an app for exploring and reviewing dog friendly spots'
# SPOT_PROJECT_SUBJECT = 'Dog'

SPOT_PROJECT_FAVICON_URL = os.path.join(MEDIA_ROOT, SPOT_PROJECT_NAME, 'favicon.ico')
SPOT_PROJECT_BRAND_LOGO_URL = os.path.join('media', SPOT_PROJECT_NAME, SPOT_PROJECT_NAME + '_logo.png')
SPOT_PROJECT_CERTIFICATE_LOGO_URL = os.path.join(MEDIA_ROOT, SPOT_PROJECT_NAME, SPOT_PROJECT_NAME + '_certificate.png')
