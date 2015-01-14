from .common import *
import os


DEBUG = True
TEMPLATE_DEBUG = True

# /home/ubuntu/<INSTANCE>/mbf/demo
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_PATH = '/'.join(PROJECT_ROOT_PATH.split("/")[:-2])
# /home/ubuntu/<INSTANCE>/mbf/mbf/media/
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
# STATIC_ROOT is defined in <INSTANCE> specific settings file and has form
# '/home/ubuntu/<INSTANCE>/public_html/'
STATIC_URL = '/static/'

# remember about APACHE-mappings in files see: /etc/apache2/sites-available/00<N>-<INSTANCE>.eu.conf
SPOT_PROJECT_FAVICON_URL = os.path.join(MEDIA_ROOT, SPOT_PROJECT_NAME, 'favicon.ico')

SPOT_PROJECT_BRAND_LOGO_URL = os.path.join(MEDIA_ROOT, SPOT_PROJECT_NAME, 'logo.svg')

SPOT_PROJECT_CERTIFICATE_LOGO_URL = os.path.join(MEDIA_ROOT, SPOT_PROJECT_NAME, SPOT_PROJECT_NAME + '_certificate.png')

if 'dogspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .dogspot import *

elif 'momspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .momspot import *

elif 'enabledspot.eu' in PROJECT_ROOT_PATH.split('/'):
    from .enabledspot import *

elif 'gayfriendlyspots.com' in PROJECT_ROOT_PATH.split('/'):
    from .gayfriendlyspots import *

elif 'veganspot.org' in PROJECT_ROOT_PATH.split('/'):
    from .veganspot import *
