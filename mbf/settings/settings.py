
from .common import *
import os


DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dogspot',
        'USER': 'dogspot',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}

# /home/ubuntu/<INSTANCE>/mbf/demo
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

# /home/ubuntu/<INSTANCE>/mbf/mbf/media/
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
# STATIC_ROOT is defined in <INSTANCE> specific settings file and has form
# '/home/ubuntu/<INSTANCE>/public_html/'
STATIC_URL = '/static/'

# remember about APACHE-mappings in files see: /etc/apache2/sites-available/00<N>-<INSTANCE>.eu.conf
