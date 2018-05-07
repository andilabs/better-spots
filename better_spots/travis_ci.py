from better_spots.settings import *
from .common_testing import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME':     'better_spots',
        'USER':     'postgres',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}
