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

SPOT_PROJECT_INSTAGRAM_URL = "https://www.instagram.com/momspoteu/"


TAGS = {
    1: "baby changing facilites",
    2: "playroom for kids",
    3: "kids menu",
}
