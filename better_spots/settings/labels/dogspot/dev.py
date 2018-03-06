from .base import *


SPOT_PROJECT_NAME = 'dogspot'

DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'localhost.debug@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
POSTGIS_VERSION = (2, 1, 3)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

MEDIA_ROOT = '/better_spots/media/'
MEDIA_URL = '/media/'
