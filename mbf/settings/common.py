#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

AUTH_USER_MODEL = 'accounts.User'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'kq$$wn#ff0qt)j7mm!d$6cee22e7hw9z#i11-@g1qaya^o!gnj')

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

ALLOWED_HOSTS = ['*']

FORMAT_MODULE_PATH = 'mbf.formats'

DESIRED_PASSWORD_LENGTH = 5

MAX_SPOTS_PER_PAGE_API = 20

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.staticfiles',


    'debug_toolbar',
    'django_celery_results',
    'django_extensions',
    'django_filters',
    'easy_thumbnails',
    'image_cropping',
    'raven.contrib.django.raven_compat',
    'solo',


    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',


    'accounts',
    'api',
    'api2',
    'blog',
    'core',
    'utils',
    'www',

)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated'
    ],
    'PAGE_SIZE': 10,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mbf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'django.template.context_processors.media',
                'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

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


THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

IMAGE_CROPPING_SIZE_WARNING = True

SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson", 
}


CELERY_RESULT_BACKEND = 'django-cache'
