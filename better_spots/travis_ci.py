from better_spots.settings import *


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

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = os.environ['MAILTRAP_USER']
EMAIL_HOST_PASSWORD = os.environ['MAILTRAP_PASSWORD']
EMAIL_PORT = '2525'
