"""
Django settings for mbf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

AUTH_USER_MODEL = 'demo.DogspotUser'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kq$$wn#ff0qt)j7mm!d$6cee22e7hw9z#i11-@g1qaya^o!gnj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

if DEBUG:
    DOGSPOT_DOMAIN = "127.0.0.1:8000"
else:
    DOGSPOT_DOMAIN = "dogspot.eu"


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '127.0.0.1:8000', 'localhost:8000', '*', '.dogspot.eu', '.dogspot.eu.']

FORMAT_MODULE_PATH = 'mbf.formats'


DESIRED_PASSWORD_LENGTH = 5
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'demo.authentication.ExpiringTokenAuthentication',
    ),
}
# Application definition
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "django.contrib.messages.context_processors.messages",

)

RAVEN_CONFIG = {
    'dsn': 'https://4fa3854da7cd48f1a8b7a14a349d251d:c9cd00443c434d5fb1b204d8e5a95ffa@app.getsentry.com/29551',
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    #'social.apps.django_app.default',
    #'bootstrap_toolkit',
    'bootstrap3_datetime',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    'django.contrib.gis',
    #'datetimewidget',
    'bootstrap3',
    'demo',
    #'import_export',
    'django.contrib.gis',
    'rest_framework',
    # 'south',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mbf.urls'

WSGI_APPLICATION = 'mbf.wsgi.application'

LANGUAGES = (
    ('pl', ('Polish')),
    ('de', ('German')),
    ('en', ('English')),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dogspot',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dogspot',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}
# DATABASES = {
#     'default': {
# 	'ENGINE': 'django.contrib.gis.db.backends.postgis',
# #        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'dogspot',                      # Or path to database file if using sqlite3.
#         # The following settings are not used with sqlite3:
#         'USER': 'dogspot',
#         'PASSWORD': 'c9c38a6dc8cdb66a0c416a9e1f8eac21',
#         'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '5432',                      # Set to empty string for default.
#     }
# }


AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
# EMAIL_HOST_USER = 'andi@dogspot.eu'
# EMAIL_HOST_PASSWORD = 'P@ssw0rd'

TOKEN_EXPIRES_AFTER = 24
EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS = 48

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
MEDIA_ROOT = '/home/ubuntu/dogspot.eu/mbf/' #os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
