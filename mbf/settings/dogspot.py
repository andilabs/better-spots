#!/usr/bin/python
# -*- coding: utf-8 -*-

INSTANCE_DOMAIN = "dogspot.eu"

# EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
# EMAIL_HOST_USER = 'andi@dogspot.eu'
# EMAIL_HOST_PASSWORD = 'P@ssw0rd'

STATIC_ROOT = '/home/ubuntu/dogspot.eu/static_assets/'
POSTGIS_VERSION = (2, 1, 2)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dogspot',
        'USER': 'dogspot',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

RAVEN_CONFIG = {
    'dsn': 'https://4fa3854da7cd48f1a8b7a14a349d251d:c9cd00443c434d5fb1b204d8e5a95ffa@app.getsentry.com/29551',
}

SPOT_PROJECT_NAME = 'dogspot'

SPOT_PROJECT_BRAND_LOGO = ''

SPOT_PROJECT_CERTIFICATE_LOGO = ''

SPOT_PROJECT_SLOGAN = ''

SPOT_PROJECT_DESCRIPTION = 'Is an app for exploring and reviewing dog friendly spots'

SPOT_PROJECT_SUBJECT = ''
