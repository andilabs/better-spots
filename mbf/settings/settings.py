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
    from mbf.settings.instance_configs.dogspot import *
    SPOT_PROJECT_NAME = 'dogspot'


elif 'momspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from mbf.settings.instance_configs.momspot import *
    SPOT_PROJECT_NAME = 'momspot'


elif 'enabledspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from mbf.settings.instance_configs.enabledspot import *
    SPOT_PROJECT_NAME = 'enabledspot'


elif 'veganspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from mbf.settings.instance_configs.veganspot import *
    SPOT_PROJECT_NAME = 'veganspot'

else:
    from .local import *

SPOT_PROJECT_FAVICON_URL = os.path.join(
    'static',
    SPOT_PROJECT_NAME,
    'favicon.ico'
)

SPOT_PROJECT_BLOGGER_PHOTO = os.path.join(
    MEDIA_URL, SPOT_PROJECT_NAME, 'bloger_photo.jpg')

TEMPLATE_DIRS = (
     os.path.join(PROJECT_ROOT_PATH, 'templates/'),
)

SPOT_FACILITIES = [d['name'] for d in HSTORE_SCHEMA]

SPOT_FACILITIES_VERBOSE_NAMES = [
    (d['kwargs']['verbose_name'], d['name']) for d in HSTORE_SCHEMA]
