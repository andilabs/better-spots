
# from .common import *


# DEBUG = False
# TEMPLATE_DEBUG = False

# # /home/ubuntu/<INSTANCE>/mbf/demo
# PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

# # /home/ubuntu/<INSTANCE>/mbf/mbf/media/
# MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
# MEDIA_URL = '/media/'
# # STATIC_ROOT is defined in <INSTANCE> specific settings file and has form
# # '/home/ubuntu/<INSTANCE>/public_html/'
# STATIC_URL = '/static/'

# # remember about APACHE-mappings in files see: /etc/apache2/sites-available/00<N>-<INSTANCE>.eu.conf

# # if PROJECT_ROOT_PATH.split('/')[3] == 'dogspot.eu':
# from .dogspot import *

# # elif PROJECT_ROOT_PATH.split('/')[3] == 'momspot.eu':
# #     from .momspot import *

# # elif PROJECT_ROOT_PATH.split('/')[3] == 'enabledspot.eu':
# #     from .enabledspot import *

# # elif PROJECT_ROOT_PATH.split('/')[3] == 'gayfriendlyspots.com':
# #     from .gayfriendlyspots import *

from .common import *
import os


DEBUG = True
TEMPLATE_DEBUG = True

# /home/ubuntu/<INSTANCE>/mbf/demo
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# /home/ubuntu/<INSTANCE>/mbf/mbf/media/
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
# STATIC_ROOT is defined in <INSTANCE> specific settings file and has form
# '/home/ubuntu/<INSTANCE>/public_html/'
STATIC_URL = '/static/'

# remember about APACHE-mappings in files see: /etc/apache2/sites-available/00<N>-<INSTANCE>.eu.conf

# if 'dogspot.eu' in PROJECT_ROOT_PATH.split('/'):
#     from .dogspot import *

# elif 'momspot.eu' in PROJECT_ROOT_PATH.split('/'):
from .dogspot import *

# else:
#     from .dogspot import *

# elif PROJECT_ROOT_PATH.split('/')[3] == 'enabledspot.eu':
#     from .enabledspot import *

# elif PROJECT_ROOT_PATH.split('/')[3] == 'gayfriendlyspots.com':
#     from .gayfriendlyspots import *
