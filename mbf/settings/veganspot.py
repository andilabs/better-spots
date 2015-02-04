#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "veganspot.org"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@veganspot.org'
EMAIL_HOST_PASSWORD = 'c9c38a6dc8cdb66a0c416a9e1f8eac21'

RAVEN_CONFIG = {
    'dsn': 'https://c487d89198d844f1b3b2271833301fdd:2b007aed601c4cacaa72ce45443f3db7@app.getsentry.com/37314',
}

STATIC_ROOT = '/home/ubuntu/veganspot.org/static_assets/'
POSTGIS_VERSION = (2, 1, 2)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'veganspot',
        'USER': 'veganspot',
        'PASSWORD': 'c9c38a6dc8cdb66a0c416a9e1f8eac21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SPOT_PROJECT_NAME = 'veganspot'

SPOT_PROJECT_SLOGAN = 'And, all the world is green!'

SPOT_PROJECT_DESCRIPTION = 'Is an app for reviewing vegans and vegetarians friendly spots'

SPOT_PROJECT_SUBJECT = 'Vege'

SPOT_PROJECT_MAIN_COLOR = '#59b84d'


