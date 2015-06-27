from .common import *
import os

from unipath import Path

DEBUG = True
TEMPLATE_DEBUG = True

PROJECT_ROOT_PATH = Path(__file__).ancestor(3)

STATICFILES_DIRS = (
    PROJECT_ROOT_PATH.child('static_assets'),
)

MEDIA_URL = '/media/'

STATIC_URL = '/static/'


if 'dogspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .dogspot import *
    SPOT_PROJECT_NAME = 'dogspot'


elif 'momspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .momspot import *
    SPOT_PROJECT_NAME = 'momspot'


elif 'enabledspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .enabledspot import *
    SPOT_PROJECT_NAME = 'enabledspot'


elif 'veganspot.org' in PROJECT_ROOT_PATH.split('/'):
    from .veganspot import *
    SPOT_PROJECT_NAME = 'veganspot'


SPOT_PROJECT_FAVICON_URL = os.path.join(
    'static',
    SPOT_PROJECT_NAME,
    'favicon.ico'
)

SPOT_PROJECT_BLOGERS = os.path.join(STATIC_URL, SPOT_PROJECT_NAME, 'bloger_photo.jpg')

TEMPLATE_DIRS = (
     os.path.join(PROJECT_ROOT_PATH, 'templates/'),
)