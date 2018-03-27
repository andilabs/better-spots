from .base import *


RAVEN_CONFIG = {
    'dsn': 'https://{raven_config_sentry_key}:f75054def0234501b24baf4c512e8613@app.getsentry.com/37316'.format(
        raven_config_sentry_key=os.environ['RAVEN_CONFIG_SENTRY_KEY']
    ),
}

INSTANCE_DOMAIN = "momspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@momspot.eu'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
