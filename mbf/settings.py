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
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

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


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'social.apps.django_app.default',
    #'bootstrap_toolkit',
    'bootstrap3_datetime',
    'django_extensions',
    #'datetimewidget',
    'bootstrap3',
    'demo',
    'import_export',
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'demo.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'dogspot.sqlite3',                      # Or path to database file if using sqlite3.
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'DOGSPOT_PLAY',                      # Or path to database file if using sqlite3.
#         # The following settings are not used with sqlite3:
#         'USER': 'django',
#         'PASSWORD': 'P@ssw0rd',
#         'HOST': 'dogspot.dyndns.org',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '',                      # Set to empty string for default.
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'DOGSPOT_RETINA',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'P@ssw0rd',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}




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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreplydogspot@gmail.com'
EMAIL_HOST_PASSWORD = 'Cichosz@'

TOKEN_EXPIRES_AFTER = 24
EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS = 48
# PROJECT_DIR = os.path.dirname(__name__)
# PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))
# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
# MEDIA_URL = '/media/'
PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'static/')


# if DEBUG:
#     STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
# else:
#     STATICFILES_DIRS = (
#         os.path.join(PROJECT_DIR, 'static'),
#     )

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# )
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'site_media')
# MEDIA_URL = '/site_media/'
STATIC_URL = '/static/'

# if DEBUG:
#     STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
# else:
#     STATICFILES_DIRS = (
#         os.path.join(PROJECT_DIR, 'static'),
#     )

# BOOTSTRAP_CSS_URL = 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.2/css/bootstrap-responsive.css'#STATIC_URL + 'bootstrap-responsive.min.css'
#BOOTSTRAP_CSS_URL = 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.2/css/bootstrap-responsive.css'
