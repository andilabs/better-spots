from .common import *
import os

from unipath import Path

DEBUG = True
TEMPLATE_DEBUG = True

# /home/ubuntu/<INSTANCE>/mbf/demo
# PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_ROOT_PATH = '/'.join(PROJECT_ROOT_PATH.split("/")[:-2])
PROJECT_ROOT_PATH = Path(__file__).ancestor(3)


STATICFILES_DIRS = (
    PROJECT_ROOT_PATH.child('static_assets'),
)

# MEDIA_ROOT is defined in <INSTANCE> specific settings file and has form
# '/home/ubuntu/<INSTANCE>/media_assets/'
MEDIA_URL = '/media/'
# STATIC_ROOT is defined in <INSTANCE> specific settings file and has form
# '/home/ubuntu/<INSTANCE>/static_assets/'
STATIC_URL = '/static/'

# remember about APACHE-mappings in files see: /etc/apache2/sites-available/00<N>-<INSTANCE>.eu.conf

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


SPOT_PROJECT_FAVICON_URL = os.path.join('media', SPOT_PROJECT_NAME, SPOT_PROJECT_NAME + '_favicon.ico')
