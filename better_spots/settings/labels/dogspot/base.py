from better_spots.settings.common import *

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

SPOT_PROJECT_NAME = 'dogspot'

SPOT_PROJECT_SLOGAN = 'Wow the World!'

SPOT_PROJECT_DESCRIPTION = 'find dog friendly cafes, restaurants and more'

SPOT_PROJECT_SUBJECT = 'Dog'

SPOT_PROJECT_MAIN_COLOR = '#fcbd41'

SPOT_PROJECT_INSTAGRAM_URL = "https://www.instagram.com/dogspoteu/"

TAGS = {
    1: 'fresh water',
    2: 'dedicated menu',
    3: 'snacks',
}
