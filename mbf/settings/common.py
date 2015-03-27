#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

AUTH_USER_MODEL = 'accounts.SpotUser'

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'kq$$wn#ff0qt)j7mm!d$6cee22e7hw9z#i11-@g1qaya^o!gnj')

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

ALLOWED_HOSTS = ['*']

FORMAT_MODULE_PATH = 'mbf.formats'

DESIRED_PASSWORD_LENGTH = 5

MAX_SPOTS_PER_PAGE = 10

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'accounts.authentication.ExpiringTokenAuthentication',
    ),
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_CONTEXT_PROCESSORS += ("www.context_processors.spot_facilities", )


INSTALLED_APPS = (
    'image_cropping',
    'easy_thumbnails',
    'south',
    'django_hstore',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'django.contrib.gis',
    'bootstrap3_datetime',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    'bootstrap3',
    'import_export',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'core',
    'api',
    'www',
    'blog',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TOKEN_EXPIRES_AFTER = 24

EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS = 48

VENUE_PHOTO_SIZE = {'W': '350', 'H': '150'}
BLOGPOST_PHOTO_SIZE = {'W': '2402', 'H': '2402'}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

IMAGE_CROPPING_SIZE_WARNING = True
