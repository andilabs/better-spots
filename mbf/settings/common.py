#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

AUTH_USER_MODEL = 'demo.SpotUser'

SECRET_KEY = 'kq$$wn#ff0qt)j7mm!d$6cee22e7hw9z#i11-@g1qaya^o!gnj'

ALLOWED_HOSTS = ['*']

FORMAT_MODULE_PATH = 'mbf.formats'

DESIRED_PASSWORD_LENGTH = 5

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'demo.authentication.ExpiringTokenAuthentication',
    ),
}


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
    'south',
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
    'rest_framework',
    'accounts',
    'core',
    'api',
    'www',
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

# AUTHENTICATION_BACKENDS = (
#     'social.backends.open_id.OpenIdAuth',
#     'social.backends.google.GoogleOpenId',
#     'social.backends.google.GoogleOAuth2',
#     'social.backends.google.GoogleOAuth',
#     'social.backends.twitter.TwitterOAuth',
#     'social.backends.yahoo.YahooOpenId',
#     'django.contrib.auth.backends.ModelBackend',
# )

DEFAULT_FROM_EMAIL = 'no-reply@dogspot.eu'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TOKEN_EXPIRES_AFTER = 24
EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS = 48
